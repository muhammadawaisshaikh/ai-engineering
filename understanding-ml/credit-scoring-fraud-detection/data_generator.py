import pandas as pd
import numpy as np

def generate_transaction_data(seed=42):
    np.random.seed(seed)

    normal_data = pd.DataFrame({
        'transaction_amount': np.random.normal(loc=50, scale=10, size=500),
        'transaction_frequency': np.random.normal(loc=5, scale=1.5, size=500),
        'location_score': np.random.normal(loc=0.2, scale=0.05, size=500)
    })

    anomalies = pd.DataFrame({
        'transaction_amount': np.random.normal(loc=200, scale=50, size=10),
        'transaction_frequency': np.random.normal(loc=20, scale=5, size=10),
        'location_score': np.random.normal(loc=0.8, scale=0.1, size=10)
    })

    data = pd.concat([normal_data, anomalies], ignore_index=True)
    return data