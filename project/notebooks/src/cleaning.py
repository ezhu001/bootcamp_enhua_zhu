import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

def load_data(filepath):
    """Load raw stock data and parse dates."""
    df = pd.read_csv(filepath, parse_dates=['date'])
    df.set_index('date', inplace=True)
    return df

def handle_missing(df, method='ffill'):
    """
    Fill missing values:
    - 'ffill': Forward fill (default for time-series)
    - 'median': Fill with median (for outliers)
    """
    if method == 'ffill':
        df.fillna(method='ffill', inplace=True)
    elif method == 'median':
        for col in df.select_dtypes(include=np.number):
            df[col].fillna(df[col].median(), inplace=True)
    return df

def remove_outliers(df, threshold=3):
    """Remove extreme values using Z-score."""
    numeric_cols = df.select_dtypes(include=np.number).columns
    for col in numeric_cols:
        z = np.abs((df[col] - df[col].mean()) / df[col].std())
        df = df[z < threshold]
    return df

def normalize_volume(df):
    """Scale volume to 0-1 range (preserves other columns)."""
    scaler = MinMaxScaler()
    df['volume'] = scaler.fit_transform(df[['volume']])
    return df

def add_returns(df):
    """Add daily return column (percentage change)."""
    df['return'] = df['close'].pct_change() * 100
    return df