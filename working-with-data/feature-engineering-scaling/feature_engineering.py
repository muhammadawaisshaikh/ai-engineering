import pandas as pd
from sklearn.preprocessing import OneHotEncoder

def engineer_features(df):
    # Create an interaction feature
    df['Area'] = df['Length'] * df['Width']
    
    # Extract time features
    df['Year'] = pd.to_datetime(df['Date']).dt.year
    df['Month'] = pd.to_datetime(df['Date']).dt.month
    
    # Encode categorical features
    encoder = OneHotEncoder(sparse=False, drop='first')
    encoded_cols = encoder.fit_transform(df[['Category']])
    encoded_df = pd.DataFrame(encoded_cols, columns=encoder.get_feature_names_out(['Category']))
    
    df = pd.concat([df.drop(columns=['Category']), encoded_df], axis=1)
    
    return df