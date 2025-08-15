import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_distributions(df: pd.DataFrame):
    """
    Plots histograms for numeric features and bar plots for categorical features.
    """
    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
    categorical_cols = df.select_dtypes(include=['object']).columns

    # Numeric features
    for col in numeric_cols:
        plt.figure(figsize=(6, 4))
        sns.histplot(df[col], kde=True)
        plt.title(f'Distribution of {col}')
        plt.show()

    # Categorical features
    for col in categorical_cols:
        plt.figure(figsize=(6, 4))
        sns.countplot(x=col, data=df)
        plt.title(f'Count Plot of {col}')
        plt.xticks(rotation=45)
        plt.show()