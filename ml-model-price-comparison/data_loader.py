import pandas as pd
import os

class DataLoader:
    def __init__(self, filepaths: list):
        """
        filepaths: list of CSV file paths for different stores
        """
        self.filepaths = filepaths

    def load_data(self):
        """Load and merge datasets from multiple CSV files"""
        all_data = []
        for filepath in self.filepaths:
            try:
                # Extract store name from filename
                store_name = os.path.splitext(os.path.basename(filepath))[0]

                # Read CSV and add a store column
                df = pd.read_csv(filepath)
                df["store"] = store_name
                all_data.append(df)

                print(f" Loaded {store_name} with {df.shape[0]} rows")
            except Exception as e:
                print(f" Error loading {filepath}: {e}")

        if all_data:
            combined = pd.concat(all_data, ignore_index=True)
            print(f"\n Final merged dataset: {combined.shape[0]} rows, {combined.shape[1]} columns")
            return combined
        else:
            print(" No data loaded")
            return None
