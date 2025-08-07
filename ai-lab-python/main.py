from utils import load_sample_data, plot_distribution

def main():
    # Load dataset
    df = load_sample_data()
    print("Data Loaded:\n", df.head())

    # Visualize the target distribution
    plot_distribution(df, 'target')

if __name__ == "__main__":
    main()