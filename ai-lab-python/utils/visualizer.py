import matplotlib.pyplot as plt

def plot_distribution(df, column):
    plt.figure(figsize=(8, 4))
    df[column].value_counts().plot(kind='bar', color='skyblue')
    plt.title(f'Distribution of {column}')
    plt.xlabel(column)
    plt.ylabel('Count')
    plt.grid(True)
    plt.tight_layout()
    plt.show()