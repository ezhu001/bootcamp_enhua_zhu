# src/outliers.py

import numpy as np
import pandas as pd
from typing import Union, Tuple, Dict, Optional

def detect_outliers(
    data: pd.DataFrame,
    method: str = 'iqr',
    threshold: float = 1.5,
    columns: Optional[list] = None,
    return_type: str = 'flag'
) -> Union[pd.DataFrame, Tuple[pd.DataFrame, Dict], Dict]:
    """
    Detect, remove, or flag outliers in financial time series data.
    
    Parameters:
    -----------
    data : pd.DataFrame
        Input dataframe containing financial time series data with columns:
        ['date', 'close', 'open', 'high', 'low', 'volume']
    method : str, optional (default='iqr')
        Method for outlier detection. Options:
        - 'iqr': Interquartile Range method
        - 'zscore': Z-score method
        - 'percentile': Percentile-based method
    threshold : float, optional (default=1.5)
        Threshold multiplier for outlier detection (used differently by each method)
    columns : list, optional (default=None)
        List of columns to check for outliers. If None, checks all numeric columns.
    return_type : str, optional (default='flag')
        What to return. Options:
        - 'flag': Add outlier flags to original data (default)
        - 'remove': Return data with outliers removed
        - 'report': Return data plus outlier report
        - 'count': Return outlier counts per column
    
    Returns:
    --------
    Depending on return_type:
    - 'flag': DataFrame with outlier flags added
    - 'remove': DataFrame with outliers removed
    - 'report': Tuple of (DataFrame with flags, outlier report dict)
    - 'count': Dictionary of outlier counts per column
    
    Examples:
    ---------
    >>> df = pd.read_csv('stock_data.csv')
    >>> df_clean = detect_outliers(df, method='iqr', return_type='remove')
    >>> df_flags, report = detect_outliers(df, return_type='report')
    """
    
    # Validate input
    if not isinstance(data, pd.DataFrame):
        raise TypeError("Input data must be a pandas DataFrame")
    
    required_columns = {'date', 'close', 'open', 'high', 'low', 'volume'}
    if not required_columns.issubset(data.columns):
        missing = required_columns - set(data.columns)
        raise ValueError(f"Missing required columns: {missing}")
    
    if method not in ['iqr', 'zscore', 'percentile']:
        raise ValueError("method must be one of: 'iqr', 'zscore', 'percentile'")
    
    if return_type not in ['flag', 'remove', 'report', 'count']:
        raise ValueError("return_type must be one of: 'flag', 'remove', 'report', 'count'")
    
    # Use all numeric columns if none specified
    numeric_cols = ['close', 'open', 'high', 'low', 'volume']
    if columns is None:
        columns = numeric_cols
    else:
        # Validate specified columns exist
        invalid_cols = set(columns) - set(data.columns)
        if invalid_cols:
            raise ValueError(f"Columns not found in data: {invalid_cols}")
    
    # Make a copy of the data to avoid modifying original
    df = data.copy()
    outlier_flags = pd.DataFrame(False, index=df.index, columns=columns)
    outlier_report = {}
    
    for col in columns:
        if col not in numeric_cols:
            continue
            
        values = df[col]
        
        if method == 'iqr':
            # IQR method
            q1 = values.quantile(0.25)
            q3 = values.quantile(0.75)
            iqr = q3 - q1
            lower_bound = q1 - threshold * iqr
            upper_bound = q3 + threshold * iqr
            flags = (values < lower_bound) | (values > upper_bound)
            
        elif method == 'zscore':
            # Z-score method
            mean = values.mean()
            std = values.std()
            if std == 0:  # avoid division by zero
                flags = pd.Series(False, index=values.index)
            else:
                z_scores = (values - mean) / std
                flags = np.abs(z_scores) > threshold
                
        elif method == 'percentile':
            # Percentile method
            lower_bound = values.quantile((100 - threshold) / 200)
            upper_bound = values.quantile(1 - (100 - threshold) / 200)
            flags = (values < lower_bound) | (values > upper_bound)
        
        outlier_flags[col] = flags
        outlier_report[col] = {
            'count': flags.sum(),
            'percentage': flags.mean() * 100,
            'method': method,
            'threshold': threshold
        }
    
    # Handle return types
    if return_type == 'flag':
        # Add outlier flags to original data
        for col in columns:
            df[f'{col}_outlier'] = outlier_flags[col]
        return df
    
    elif return_type == 'remove':
        # Remove rows with any outliers
        any_outlier = outlier_flags.any(axis=1)
        return df[~any_outlier]
    
    elif return_type == 'report':
        # Add flags and return report
        for col in columns:
            df[f'{col}_outlier'] = outlier_flags[col]
        return df, outlier_report
    
    elif return_type == 'count':
        # Just return the counts
        return {col: report['count'] for col, report in outlier_report.items()}
    
    return df

def example_usage():
    """Demonstrate how to use the detect_outliers function"""
    # Create sample data
    np.random.seed(42)
    data = {
        'date': pd.date_range(start='2023-01-01', periods=100),
        'close': np.random.normal(100, 5, 100),
        'open': np.random.normal(100, 5, 100),
        'high': np.random.normal(105, 5, 100),
        'low': np.random.normal(95, 5, 100),
        'volume': np.random.lognormal(10, 1, 100)
    }
    # Add some outliers
    data['close'][10] = 200
    data['volume'][20] = 1e6
    
    df = pd.DataFrame(data)
    
    print("=== Original Data (first 5 rows) ===")
    print(df.head())
    
    print("\n=== Detecting and Flagging Outliers ===")
    df_flags = detect_outliers(df)
    print(df_flags[df_flags.filter(like='_outlier').any(axis=1)].head())
    
    print("\n=== Removing Outliers ===")
    df_clean = detect_outliers(df, return_type='remove')
    print(f"Original shape: {df.shape}, Cleaned shape: {df_clean.shape}")
    
    print("\n=== Getting Outlier Report ===")
    _, report = detect_outliers(df, return_type='report')
    for col, stats in report.items():
        print(f"{col}: {stats['count']} outliers ({stats['percentage']:.2f}%)")
    
    print("\n=== Getting Outlier Counts ===")
    counts = detect_outliers(df, return_type='count')
    print(counts)

if __name__ == "__main__":
    example_usage()