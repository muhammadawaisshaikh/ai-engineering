import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler

def scale_features(df):
    scaler_standard = StandardScaler()
    scaler_minmax = MinMaxScaler()
    
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
    
    # Standard Scaling
    df_standard_scaled = pd.DataFrame(scaler_standard.fit_transform(df[numeric_cols]), columns=numeric_cols)
    
    # Min-Max Scaling
    df_minmax_scaled = pd.DataFrame(scaler_minmax.fit_transform(df[numeric_cols]), columns=numeric_cols)
    
    return df_standard_scaled, df_minmax_scaled