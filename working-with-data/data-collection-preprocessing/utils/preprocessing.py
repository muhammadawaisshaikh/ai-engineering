import pandas as pd

def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans and preprocesses the dataset.

    Steps:
    1. Remove duplicate rows
    2. Handle missing values
    3. Reset index after cleaning

    Parameters:
        df (pd.DataFrame): Raw input DataFrame

    Returns:
        pd.DataFrame: Cleaned DataFrame
    """
    # Remove duplicate rows
    before = df.shape[0]
    df = df.drop_duplicates()
    after = df.shape[0]
    print(f"🧹 Removed {before - after} duplicate rows.")

    # Handle missing values
    missing_count = df.isnull().sum().sum()
    if missing_count > 0:
        df = df.dropna()
        print(f" Removed {missing_count} rows with missing values.")
    else:
        print("No missing values found.")

    # Reset index
    df = df.reset_index(drop=True)

    return df