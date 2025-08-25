# Currency Price Prediction Model

This project uses machine learning to predict foreign exchange rates, specifically focusing on USD to EUR conversion rates.

## What This Project Does

The goal is to build a model that can predict future currency exchange rates based on historical data. This type of prediction is useful for financial planning, trading decisions, and understanding currency market trends.

## How It Works

The project follows these main steps:

1. **Data Loading**: Imports historical currency exchange rate data from a CSV file
2. **Data Cleaning**: Removes missing values and formats dates properly
3. **Feature Creation**: Creates time-based features using past exchange rates
4. **Model Training**: Uses a Random Forest algorithm to learn patterns in the data
5. **Visualization**: Shows the historical trends in exchange rates

## Files in This Project

- `main.py` - The main script that runs the entire process
- `data_loader.py` - Handles loading the currency dataset
- `preprocess.py` - Cleans and prepares the data for analysis
- `model.py` - Contains the machine learning model and training logic
- `visualise.py` - Creates charts and graphs of the data
- `data/` - Folder containing the dataset

## Getting Started

### Prerequisites

You'll need Python installed on your computer, along with these packages:
- pandas (for data handling)
- numpy (for numerical operations)
- scikit-learn (for machine learning)
- matplotlib (for creating charts)

### Running the Project

1. Make sure you have the required packages installed
2. Place your currency dataset in the `data/` folder
3. Run the main script: `python main.py`

## Understanding the Results

The model will:
- Show you how well it can predict exchange rates
- Display a chart of historical USD to EUR rates
- Print the accuracy of predictions (measured by Mean Squared Error)

## Important Notes

- The model uses historical data to make predictions, but past performance doesn't guarantee future results
- Currency markets are influenced by many factors beyond what this model considers
- This is a learning project and should not be used for actual financial decisions

## Dataset Information

The project is designed to work with foreign exchange rate data. You can find sample datasets on platforms like Kaggle, or use your own currency data in CSV format.

## Customization

You can modify the model by:
- Changing the number of past time periods used for predictions
- Adjusting the Random Forest parameters
- Adding more features like economic indicators
- Using different machine learning algorithms
