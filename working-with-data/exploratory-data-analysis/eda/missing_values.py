import pandas as pd

def missing_values_summary(df: pd.DataFrame):
    """
    Prints a table of missing values and their percentage in each column.
    """
    missing = df.isnull().sum()
    missing_percent = (missing / len(df)) * 100
    missing_table = pd.DataFrame({
        'Missing Values': missing,
        'Percentage': missing_percent
    })
    print("\n--- Missing Values Summary ---")
    print(missing_table[missing_table['Missing Values'] > 0].sort_values(by='Percentage', ascending=False))