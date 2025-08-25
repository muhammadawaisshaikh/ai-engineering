from data_loader import DataLoader
from preprocess import Preprocessor
from visualise import Visualiser
from model import CurrencyModel

def main():
    # Step 1: Load Data
    loader = DataLoader("data/Foreign_Exchange_Rates.csv")  # Kaggle dataset
    data = loader.load_data()

    # Step 2: Preprocess Data
    preprocessor = Preprocessor(data)
    clean_data = preprocessor.clean_data()

    # Step 3: Visualize
    vis = Visualiser(clean_data)
    vis.plot_currency_trend()

    # Step 4: Train Model
    model = CurrencyModel(clean_data)
    df_features = model.create_features()
    trained_model, X_test, y_test, preds = model.train(df_features)

if __name__ == "__main__":
    main()