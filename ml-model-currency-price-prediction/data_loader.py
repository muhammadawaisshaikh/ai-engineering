import pandas as pd

class DataLoader:
    def __init__(self, filepath: str):
        self.filepath = filepath

    def load_data(self):
        """Load currency dataset from CSV file"""
        try:
            data = pd.read_csv(self.filepath)
            print(f" Data loaded successfully with {data.shape[0]} rows and {data.shape[1]} columns")
            return data
        except Exception as e:
            print(f" Error loading data: {e}")
            return None