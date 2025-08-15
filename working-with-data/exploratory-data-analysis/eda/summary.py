import pandas as pd

def dataset_summary(df: pd.DataFrame):
    """
    Print dataset shape, info, and statistical summary.
    """
    print("\n--- Dataset Shape ---")
    print(df.shape)

    print("\n--- Dataset Info ---")
    print(df.info())

    print("\n--- Statistical Summary ---")
    print(df.describe(include='all'))