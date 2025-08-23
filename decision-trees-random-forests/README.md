# Decision Trees and Random Forests

This project shows how to use decision trees and random forests for classification tasks. These are popular machine learning methods that can help predict outcomes based on input data.

## What This Project Does

The project trains two different machine learning models:
- **Decision Tree**: A simple model that makes decisions by asking yes/no questions about the data
- **Random Forest**: A more advanced model that combines many decision trees to make better predictions

Both models are tested on the same data to see which one performs better.

## Files in This Project

- `main.py` - The main script that runs the project
- `models/tree_forest.py` - Contains the functions to train the models
- `README.md` - This file explaining the project

## How to Run

1. Make sure you have Python installed on your computer
2. Install the required packages by running: `pip install scikit-learn`
3. Run the project by typing: `python main.py`

## What You'll See

When you run the project, it will:
1. Load some sample data for classification
2. Train a decision tree model
3. Train a random forest model
4. Show you how accurate each model is

The output will look something like:
```
Decision Tree Accuracy: 0.85
Random Forest Accuracy: 0.92
```

## How It Works

**Decision Trees** work by splitting data into smaller groups based on certain rules. Think of it like a flowchart that asks questions to classify things.

**Random Forests** work by creating many decision trees and then combining their answers. This usually gives better results because it reduces the chance of making mistakes.

## Why Use These Models

- They are easy to understand and explain
- They work well with both numbers and text data
- They can handle missing data
- They don't require the data to be scaled or transformed

## Learning Goals

After working with this project, you should understand:
- How decision trees make predictions
- Why random forests often work better than single trees
- How to measure how well a model performs
- Basic machine learning workflow

This is a good starting point for learning about tree-based machine learning methods.
