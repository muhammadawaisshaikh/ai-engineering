# ML Model - Price Comparison

This project compares prices across different stores using machine learning. It helps understand price differences and build a model to predict prices based on various factors.

## What This Project Does

The project loads store price data, cleans it up, looks for patterns, and builds a machine learning model to predict prices. It also compares prices between different stores to see where you might get better deals.

## Dataset

You need to download the dataset from Kaggle first:

1. Go to: https://www.kaggle.com/datasets/declanmcalinden/time-series-uk-supermarket-data
2. Download the dataset files
3. Create a `data` folder in your project directory
4. Place the CSV files in the `data` folder with names like `market1.csv`, `market2.csv`, etc.
5. The program will automatically load and combine all market data files

## Files in This Project

- `main.py` - Runs the complete analysis
- `/data` - download kaggle dataset and place multiple store csv data files in this folder
- `data_loader.py` - Loads and combines multiple store datasets from CSV files
- `data_preprocessing.py` - Cleans up the data and fixes any problems
- `exploratory_analysis.py` - Creates charts to show price patterns
- `model_builder.py` - Builds and trains the machine learning model
- `evaluation.py` - Tests how well the model works

## How to Use

1. Make sure you have Python installed
2. Install the required packages: `pip install pandas scikit-learn matplotlib seaborn`
3. Download the dataset from Kaggle (see Dataset section above)
4. Run the project: `python main.py`

## What You'll See

The program will:
- Load and combine data from multiple store CSV files
- Show charts of price distributions across all stores
- Compare prices between different stores using box plots
- Build a model to predict prices based on store and other factors
- Tell you how accurate the model is using R² score and MAE

## Requirements

- Python 3.7 or higher
- pandas
- scikit-learn
- matplotlib
- seaborn

## Notes

- Make sure your CSV files have a 'prices_(£)' column
- The program automatically adds a 'store' column to identify which store each price comes from
- The model works best with clean, complete data from all stores
- You can change the test size in `model_builder.py` if you want to test on more or less data
- The program expects CSV files named `market1.csv`, `market2.csv`, etc. in the `data` folder
