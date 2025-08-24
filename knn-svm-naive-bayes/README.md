# KNN, SVM, and Naive Bayes Models

This folder contains three different machine learning models that can be used for classification tasks.

## What are these models?

### KNN (K-Nearest Neighbors)
KNN is a simple model that looks at the data points closest to the one you want to predict. It finds the K nearest neighbors and makes a decision based on what most of them are. Think of it like asking your closest neighbors for advice.

### SVM (Support Vector Machine)
SVM tries to find the best line or boundary that separates different groups of data. It looks for the widest possible gap between groups, making it good at finding clear dividing lines in your data.

### Naive Bayes
Naive Bayes uses probability to make predictions. It looks at how often different features appear with each class and uses that information to guess which class a new data point belongs to.

## Files in this folder

- `main.py` - The main program that runs all three models
- `knn_model.py` - Contains the KNN model code
- `svm_model.py` - Contains the SVM model code  
- `naive_bayes_model.py` - Contains the Naive Bayes model code
- `visualize/` - Folder with tools to see how the models work

## How to use

1. Make sure you have Python installed
2. Install the required packages (see requirements below)
3. Run `python main.py` to test all three models
4. Use the visualization tools to see how each model makes decisions

## Required packages

- scikit-learn (for the machine learning models)
- numpy (for working with numbers)
- matplotlib (for creating graphs and charts)

## What these models are good for

- **KNN**: Good for simple problems where similar things are close together
- **SVM**: Good for problems where you can clearly separate different groups
- **Naive Bayes**: Good for text classification and problems with many features

## Example use cases

- Classifying emails as spam or not spam
- Identifying different types of flowers based on measurements
- Predicting whether a customer will buy a product
- Sorting documents into different categories
