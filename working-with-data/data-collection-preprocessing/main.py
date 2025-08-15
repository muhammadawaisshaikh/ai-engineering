from utils.data_loader import load_dataset
from utils.preprocessing import preprocess_data

def main():
    # Step 1: Load raw dataset
    df = load_dataset("data/creditcard.csv")
    print(f" Raw dataset shape: {df.shape}")

    # Step 2: Preprocess data
    df = preprocess_data(df)
    print(f" Cleaned dataset shape: {df.shape}")

    # Step 3: Preview first 5 rows
    print("\n Sample Data:")
    print(df.head())

if __name__ == "__main__":
    main()