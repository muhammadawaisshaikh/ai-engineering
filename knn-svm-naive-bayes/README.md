# KNN, SVM, and Naive Bayes Models

A comprehensive implementation of three fundamental classification algorithms with evaluation metrics, visualization tools, and decision boundary analysis for understanding how these models make classification decisions.

## Overview

This folder contains three different machine learning models that can be used for classification tasks, along with comprehensive tools for evaluation and visualization. Each algorithm represents a different approach to classification, providing insights into various machine learning paradigms.

## What are these models?

### KNN (K-Nearest Neighbors)
KNN is a simple, instance-based learning algorithm that classifies objects based on the majority class of their k nearest neighbors in the feature space. It's a non-parametric method that makes no assumptions about the underlying data distribution.

**Key Characteristics:**
- **Lazy Learning**: No training phase, predictions made at query time
- **Distance-Based**: Uses Euclidean or other distance metrics
- **Local Approximation**: Assumes similar instances belong to similar classes
- **Parameter k**: Number of neighbors to consider for classification

### SVM (Support Vector Machine)
SVM tries to find the optimal hyperplane that separates different classes with the maximum margin. It's particularly effective for high-dimensional data and can handle both linear and non-linear classification through kernel functions.

**Key Characteristics:**
- **Margin Maximization**: Finds the widest possible gap between classes
- **Kernel Methods**: Can handle non-linear decision boundaries
- **Regularization**: Built-in overfitting prevention through margin control
- **Support Vectors**: Only a subset of training points influence the decision boundary

### Naive Bayes
Naive Bayes uses probability theory and Bayes' theorem to make predictions. It assumes conditional independence between features given the class, making it computationally efficient and often surprisingly effective.

**Key Characteristics:**
- **Probabilistic**: Provides probability estimates for predictions
- **Feature Independence**: Assumes features are conditionally independent
- **Fast Training**: Simple probability calculations
- **Interpretable**: Easy to understand decision process

## Project Structure

### Core Model Files
- `main.py` - The main program that runs all three models
- `knn_model.py` - Contains the KNN model implementation
- `svm_model.py` - Contains the SVM model implementation  
- `naive_bayes_model.py` - Contains the Naive Bayes model implementation

### Visualization and Evaluation
- `visualize/` - Folder with tools to see how the models work and make decisions
  - `main.py` - Orchestrates visualization demonstrations
  - `models.py` - Model training for visualization
  - `visualize_boundaries.py` - Decision boundary plotting functions
- `evaluation-metrics-accuracy, precision, recall/` - Comprehensive evaluation tools
  - `data_loader.py` - Dataset preparation
  - `models_knn_svm_nb.py` - Model training functions
  - `evaluation.py` - Performance metrics calculation
  - `visualization.py` - Decision boundary and metrics visualization

## How to use

### Prerequisites
1. Make sure you have Python installed on your computer
2. Install the required packages by running: `pip install scikit-learn numpy matplotlib pandas`
3. Ensure all subdirectories and files are present

### Basic Usage
Run the main program to test all three models:
```bash
python main.py
```

### Visualization
Explore decision boundaries and model behavior:
```bash
cd visualize
python main.py
```

### Evaluation Metrics
Analyze model performance comprehensively:
```bash
cd evaluation-metrics-accuracy, precision, recall
python main.py
```

## What You'll See

When you run the project, it will:
1. Load sample data for classification (Iris dataset)
2. Train a KNN model with k=3 neighbors
3. Train an SVM model with linear kernel
4. Train a Naive Bayes model
5. Show accuracy scores for each model

The output will look something like:
```
KNN Accuracy: 0.97
SVM Accuracy: 0.96
Naive Bayes Accuracy: 0.95
```

## How It Works

### KNN Classification Process
1. **Distance Calculation**: Compute distances between query point and all training points
2. **Neighbor Selection**: Find k nearest neighbors based on distance
3. **Majority Voting**: Classify based on most common class among neighbors
4. **Tie Breaking**: Handle cases where classes are equally represented

### SVM Classification Process
1. **Feature Space Mapping**: Transform data into high-dimensional space
2. **Margin Optimization**: Find hyperplane with maximum margin between classes
3. **Support Vector Identification**: Identify critical training points
4. **Decision Boundary**: Use support vectors to define classification boundary

### Naive Bayes Classification Process
1. **Prior Probability**: Calculate class probabilities from training data
2. **Likelihood Calculation**: Estimate feature probabilities for each class
3. **Posterior Computation**: Apply Bayes' theorem to compute class probabilities
4. **Classification**: Assign class with highest posterior probability

## Why Use These Models

### KNN Advantages
- **Simple and Intuitive**: Easy to understand and implement
- **No Training Phase**: Can handle dynamic datasets
- **Non-linear Boundaries**: Can capture complex decision boundaries
- **Few Parameters**: Only need to tune k value

### SVM Advantages
- **High Dimensional Performance**: Works well with many features
- **Kernel Flexibility**: Can handle non-linear relationships
- **Margin Maximization**: Good generalization performance
- **Regularization**: Built-in overfitting prevention

### Naive Bayes Advantages
- **Fast Training**: Efficient probability calculations
- **Small Datasets**: Works well with limited training data
- **Feature Independence**: Robust to irrelevant features
- **Probability Output**: Provides confidence scores

## Learning Goals

After working with this project, you should understand:

1. **How KNN makes predictions**: Distance-based classification and neighbor voting
2. **How SVM finds decision boundaries**: Margin maximization and support vectors
3. **How Naive Bayes calculates probabilities**: Bayes' theorem and feature independence
4. **How to measure model performance**: Accuracy, precision, recall, and F1-score
5. **How to visualize decision boundaries**: Understanding model decision regions
6. **Basic machine learning workflow**: Data preparation, training, evaluation, visualization

## Customization and Extension

### Parameter Tuning
- **KNN**: Adjust k value, try different distance metrics
- **SVM**: Experiment with different kernels, adjust C parameter
- **Naive Bayes**: Try different probability distributions

### Feature Engineering
- Add new features to improve classification
- Implement feature selection methods
- Create interaction features
- Handle categorical variables

### Model Evaluation
- Implement cross-validation
- Add more evaluation metrics
- Create confusion matrices
- Generate ROC curves

## Example Use Cases

These models are ideal for:
- **Email Classification**: Spam vs. legitimate email detection
- **Medical Diagnosis**: Disease classification based on symptoms
- **Customer Segmentation**: Grouping customers by behavior
- **Document Classification**: Categorizing text documents
- **Image Classification**: Basic image recognition tasks
- **Credit Risk Assessment**: Loan approval decisions

## Real-World Applications

### KNN Applications
- **Recommendation Systems**: Finding similar users or products
- **Pattern Recognition**: Handwriting and image recognition
- **Medical Diagnosis**: Symptom-based disease classification
- **Financial Analysis**: Credit scoring and fraud detection

### SVM Applications
- **Text Classification**: Document categorization and sentiment analysis
- **Bioinformatics**: Protein classification and gene expression analysis
- **Computer Vision**: Image classification and object detection
- **Financial Forecasting**: Stock price prediction and risk assessment

### Naive Bayes Applications
- **Spam Filtering**: Email classification systems
- **Medical Diagnosis**: Disease prediction from symptoms
- **Sentiment Analysis**: Social media sentiment classification
- **News Classification**: Article categorization

## Performance Considerations

### KNN Performance
- **Training Time**: O(1) - no training required
- **Prediction Time**: O(n) - scales with dataset size
- **Memory Usage**: O(n) - stores all training data
- **Scalability**: Limited by dataset size

### SVM Performance
- **Training Time**: O(n²) to O(n³) - depends on algorithm
- **Prediction Time**: O(s) - scales with support vectors
- **Memory Usage**: O(s) - stores support vectors only
- **Scalability**: Good for high-dimensional data

### Naive Bayes Performance
- **Training Time**: O(n×f) - scales with data size and features
- **Prediction Time**: O(f) - scales with number of features
- **Memory Usage**: O(c×f) - stores probability tables
- **Scalability**: Excellent for large datasets

## Best Practices

### Data Preparation
- **Feature Scaling**: Normalize features for KNN and SVM
- **Missing Values**: Handle missing data appropriately
- **Feature Selection**: Remove irrelevant features
- **Data Quality**: Ensure clean, consistent data

### Model Selection
- **Dataset Size**: KNN for small datasets, SVM for medium, Naive Bayes for large
- **Feature Count**: SVM excels with many features
- **Linearity**: Consider data linearity for kernel selection
- **Interpretability**: Choose based on explanation requirements

### Evaluation Strategy
- **Cross-Validation**: Use k-fold cross-validation for reliable estimates
- **Multiple Metrics**: Don't rely on accuracy alone
- **Baseline Comparison**: Compare against simple baselines
- **Business Context**: Consider practical implications

## Troubleshooting

### Common Issues
- **Poor KNN Performance**: Check feature scaling and distance metrics
- **SVM Convergence**: Adjust C parameter and kernel selection
- **Naive Bayes Bias**: Handle class imbalance and feature independence
- **Memory Problems**: Use data sampling for large datasets

### Performance Tips
- **Vectorization**: Use numpy operations for faster computation
- **Data Types**: Use appropriate data types to save memory
- **Early Stopping**: Implement convergence criteria for large datasets
- **Parallel Processing**: Use joblib for parallel cross-validation

## Next Steps

After mastering these classification algorithms:

1. **Ensemble Methods**: Learn Random Forests and Gradient Boosting
2. **Neural Networks**: Explore deep learning approaches
3. **Advanced SVM**: Study kernel methods and parameter tuning
4. **Feature Engineering**: Master advanced feature creation techniques
5. **Model Interpretability**: Understand how to explain model decisions

## Contributing

We welcome improvements to these implementations:
- Better parameter tuning strategies
- Additional evaluation metrics
- Enhanced visualization capabilities
- Performance optimizations
- Documentation improvements

## Resources

- **Scikit-learn Documentation**: https://scikit-learn.org/stable/
- **Pattern Recognition**: "Pattern Recognition and Machine Learning" by Bishop
- **Machine Learning**: "The Elements of Statistical Learning" by Hastie et al.
- **Online Courses**: Coursera Machine Learning by Andrew Ng

---

*This project provides a solid foundation for understanding fundamental classification algorithms. Master these methods to build more sophisticated machine learning systems and tackle real-world classification problems effectively.*
