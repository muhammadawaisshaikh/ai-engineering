import pandas as pd
from eda.summary import dataset_summary
from eda.distributions import plot_distributions
from eda.missing_values import missing_values_summary
from eda.correlation import correlation_heatmap

if __name__ == "__main__":
    # Load sample dataset (Iris dataset for demonstration)
    df = pd.read_csv("data/iris.csv")

    # 1. Dataset Summary
    dataset_summary(df)

    # 2. Plot Distributions
    plot_distributions(df)

    # 3. Missing Values Analysis
    missing_values_summary(df)

    # 4. Correlation Analysis
    correlation_heatmap(df)