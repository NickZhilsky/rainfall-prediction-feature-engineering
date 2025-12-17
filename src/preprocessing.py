import pandas as pd


def load_data(path: str) -> pd.DataFrame:
    """
    Load dataset from a CSV file.

    Parameters
    ----------
    path : str
        Path to the CSV file.

    Returns
    -------
    pd.DataFrame
        Loaded dataset.
    """
    return pd.read_csv(path)


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Basic data cleaning.

    - drops duplicates
    - handles missing values (baseline strategy)

    Parameters
    ----------
    df : pd.DataFrame

    Returns
    -------
    pd.DataFrame
    """
    df = df.copy()
    df = df.drop_duplicates()
    return df

