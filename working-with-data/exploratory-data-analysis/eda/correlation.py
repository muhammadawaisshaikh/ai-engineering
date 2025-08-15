import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def correlation_heatmap(df: pd.DataFrame):
    """
    Plots a heatmap of correlations for numeric features.
    """
    corr = df.corr(numeric_only=True)
    plt.figure(figsize=(10, 6))
    sns.heatmap(corr, annot=True, cmap='coolwarm')
    plt.title('Feature Correlation Heatmap')
    plt.show()