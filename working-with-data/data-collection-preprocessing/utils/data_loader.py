import pandas as pd

def load_dataset(path: str) -> pd.DataFrame:
    """
    Loads the dataset from a given file path.

    Parameters:
        path (str): The path to the CSV file.

    Returns:
        pd.DataFrame: The loaded dataset as a pandas DataFrame.
    """
    try:
        df = pd.read_csv(path)
        print(f" Data successfully loaded from {path}")
        return df
    except FileNotFoundError:
        print(f" Error: File not found at {path}")
        raise