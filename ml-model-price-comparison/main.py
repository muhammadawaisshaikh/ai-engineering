from data_loader import DataLoader
from data_preprocessing import DataPreprocessor
from exploratory_analysis import ExploratoryAnalysis
from model_builder import ModelBuilder
from evaluation import Evaluation

def main():
    # Step 1: Load data (5 market CSVs)
    filepaths = [
        "data/All_Data_Tesco.csv",
        "data/All_Data_Sains.csv",
        "data/All_Data_Morrisons.csv",
        "data/All_Data_Aldi.csv",
        "data/All_Data_ASDA.csv"
    ]
    loader = DataLoader(filepaths)
    data = loader.load_data()

    if data is None:
        return

    # Step 2: Preprocess data
    preprocessor = DataPreprocessor(data)
    data = preprocessor.clean_data()
    data = preprocessor.encode_data()

    # Step 3: Exploratory analysis
    analysis = ExploratoryAnalysis(data)
    analysis.price_distribution()
    analysis.store_comparison()

    # Step 4: Train model
    builder = ModelBuilder(data)
    model, X_test, y_test = builder.train_model()

    # Step 5: Evaluate
    evaluator = Evaluation(model, X_test, y_test)
    evaluator.evaluate()

if __name__ == "__main__":
    main()