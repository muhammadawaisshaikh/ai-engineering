import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

class CurrencyModel:
    def __init__(self, data: pd.DataFrame):
        self.data = data
        self.model = RandomForestRegressor(n_estimators=100, random_state=42)

    def create_features(self, window_size=5):
        """Convert time series into supervised learning format"""
        df = self.data.copy()
        for i in range(1, window_size+1):
            df[f'lag_{i}'] = df['USD_EUR'].shift(i)
        df.dropna(inplace=True)
        return df

    def train(self, df):
        """Train Random Forest model"""
        X = df.drop(columns=['Date', 'USD_EUR'])
        y = df['USD_EUR']

        split = int(0.8 * len(df))
        X_train, X_test = X[:split], X[split:]
        y_train, y_test = y[:split], y[split:]

        self.model.fit(X_train, y_train)
        preds = self.model.predict(X_test)

        mse = mean_squared_error(y_test, preds)
        print(f" Model trained. Test MSE: {mse:.5f}")

        return self.model, X_test, y_test, preds