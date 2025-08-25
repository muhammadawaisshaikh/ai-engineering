import pandas as pd
import numpy as np

class Preprocessor:
    def __init__(self, data: pd.DataFrame):
        self.data = data

    def clean_data(self):
        """Preprocess dataset: handle missing values, date formatting"""
        df = self.data.copy()
        df.rename(columns={"Time Serie": "Date"}, inplace=True)

        # Convert date
        df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

        # Replace 'ND' values with NaN
        df = df.replace('ND', np.nan)
        
        # Convert USD_EUR column to numeric, coercing errors to NaN
        df['EURO AREA - EURO/US$'] = pd.to_numeric(df['EURO AREA - EURO/US$'], errors='coerce')

        # Drop missing values
        df.dropna(inplace=True)

        # Example: Keep only USD/EUR rates
        df = df[['Date', 'EURO AREA - EURO/US$']]
        df.rename(columns={"EURO AREA - EURO/US$": "USD_EUR"}, inplace=True)

        return df