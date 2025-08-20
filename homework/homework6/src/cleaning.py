# src/cleaning.py
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

def fill_missing_median(df, columns=None):
    """
    Fill missing numeric values with the median of each column.

    Parameters
    ----------
    df : pd.DataFrame
        Input DataFrame containing data.
    columns : list, optional
        List of columns to fill. If None, all numeric columns are considered.

    Returns
    -------
    pd.DataFrame
        DataFrame with missing values in specified numeric columns filled.

    Assumptions
    -----------
    - Only numeric columns for filling with medians.
    - Non-numeric columns are ignored in general.
    - A full NaN column will leade to any fill be NaN.
    """
    if columns is None:
        columns = df.select_dtypes(include=np.number).columns
    
    for col in columns:
        if col in df.columns:
            df[col] = df[col].fillna(df[col].median())
    
    return df


def drop_missing(df, threshold=0.5):
    """
    Drop columns whose proportion of missing values exceeds a threshold.

    Parameters
    ----------
    df : pd.DataFrame
        Input DataFrame containing data.
    threshold : float, default=0.5
        Maximum allowable fraction of missing values per column.
        Columns with missingness > threshold are dropped.

    Returns
    -------
    pd.DataFrame
        DataFrame with high-missingness columns removed.

    Assumptions
    -----------
    - Threshold is stated, like 50% here.
    - Entire columns are dropped, not individual rows.
    """
    missing_percent = df.isnull().mean()
    columns_to_drop = missing_percent[missing_percent > threshold].index
    df = df.drop(columns=columns_to_drop)
    return df


def normalize_data(df, columns=None):
    """
    Normalize numeric values to [0, 1] range using Min-Max scaling.

    Parameters
    ----------
    df : pd.DataFrame
        Input DataFrame containing data.
    columns : list, optional
        Columns to normalize. If None, all numeric columns are normalized.

    Returns
    -------
    pd.DataFrame
        DataFrame with specified columns normalized between 0 and 1.

    Assumptions
    -----------
    - Works only on numeric columns; raise errors for non-numeric ones.
    - If a column has constant values, MinMaxScaler will scale all values to 0.
    """
    if columns is None:
        columns = df.select_dtypes(include=np.number).columns
    
    scaler = MinMaxScaler()
    df[columns] = scaler.fit_transform(df[columns])
    
    return df
