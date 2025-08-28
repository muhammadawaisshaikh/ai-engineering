# Model Utilities

This directory contains utility functions for training, saving, and loading machine learning models. These utilities provide a consistent interface for model management across different deployment methods.

## Files

- `train_model.py` - Model training script
- `save_load.py` - Model persistence utilities
- `main.py` - Main execution script

## Overview

The utilities provide:
- **Model Training**: Train a simple Iris flower classifier
- **Model Persistence**: Save and load trained models using joblib
- **Model Testing**: Test loaded models with sample data
- **Consistent Interface**: Same functions work across all deployment methods

## Model Training

### `train_model.py`

This script trains a simple machine learning model on the Iris dataset:

```python
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

def train_model():
    # Load the Iris dataset
    iris = load_iris()
    X, y = iris.data, iris.target
    
    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train a Random Forest classifier
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    return model
```

**Features:**
- Uses Random Forest classifier for robust predictions
- Includes train-test split for model validation
- Sets random seed for reproducible results
- Returns trained model ready for deployment

## Model Persistence

### `save_load.py`

Provides functions for saving and loading trained models:

#### `save_model(model, path)`
- Saves a trained model to disk using joblib
- Creates directory structure if it doesn't exist
- Supports custom file paths
- Prints confirmation message

#### `load_model(path)`
- Loads a saved model from disk
- Returns the loaded model ready for inference
- Prints confirmation message
- Handles path resolution automatically

**Usage Example:**
```python
from save_load import save_model, load_model

# Save a trained model
model = train_model()
save_model(model, "./models/iris_model.pkl")

# Load the saved model
loaded_model = load_model("./models/iris_model.pkl")
```

## Main Execution

### `main.py`

The main script demonstrates the complete workflow:

1. **Train the model** using the training function
2. **Save the model** to disk for later use
3. **Load the model** to verify persistence
4. **Test the model** with sample input data

**Execution:**
```bash
python main.py
```

**Output:**
```
Model saved at ./models/iris_model.pkl
Model loaded from ./models/iris_model.pkl
Prediction for [[5.1, 3.5, 1.4, 0.2]]: [0]
```

## Model Details

### Dataset
- **Source**: Scikit-learn built-in Iris dataset
- **Features**: 4 numerical features (sepal/petal length/width)
- **Target**: 3 flower species (0: setosa, 1: versicolor, 2: virginica)
- **Size**: 150 samples, 50 per class

### Algorithm
- **Classifier**: Random Forest
- **Trees**: 100 decision trees
- **Random State**: 42 (for reproducibility)
- **Performance**: Typically achieves 95%+ accuracy

### Input Format
The model expects input as a 2D array with 4 features:
```python
features = [[sepal_length, sepal_width, petal_length, petal_width]]
```

### Output Format
Returns predicted class labels as a 1D array:
```python
prediction = model.predict(features)  # e.g., [0] for setosa
```

## Customization

### Using Different Models

To use a different algorithm:

```python
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier

def train_svm_model():
    model = SVC(kernel='rbf', random_state=42)
    # ... training code ...
    return model

def train_neural_network():
    model = MLPClassifier(hidden_layer_sizes=(100, 50), random_state=42)
    # ... training code ...
    return model
```

### Using Different Datasets

To adapt for other datasets:

```python
def train_custom_model(dataset_path):
    # Load your custom dataset
    data = pd.read_csv(dataset_path)
    X = data.drop('target', axis=1)
    y = data['target']
    
    # Train model
    model = RandomForestClassifier(random_state=42)
    model.fit(X, y)
    
    return model
```

### Custom Model Paths

Modify the default paths in `save_load.py`:

```python
# Change default model location
DEFAULT_MODEL_PATH = "./custom_models/my_model.pkl"

def save_model(model, path=DEFAULT_MODEL_PATH):
    # ... implementation ...

def load_model(path=DEFAULT_MODEL_PATH):
    # ... implementation ...
```

## Error Handling

The utilities include basic error handling:

- **Directory Creation**: Automatically creates model directories
- **File Existence**: Checks if model files exist before loading
- **Import Validation**: Ensures required libraries are available

## Dependencies

Required packages:
- **scikit-learn**: For machine learning algorithms and datasets
- **joblib**: For efficient model serialization
- **numpy**: For numerical operations (included with scikit-learn)
- **pandas**: For data manipulation (optional, for custom datasets)

## Best Practices

### Model Versioning
- Use descriptive filenames with timestamps
- Keep multiple model versions for comparison
- Document model performance and parameters

### Path Management
- Use relative paths for portability
- Consider environment-specific configurations
- Validate file paths before operations

### Performance
- Use joblib for efficient serialization
- Consider model compression for large models
- Cache loaded models when possible

## Troubleshooting

### Common Issues

- **Import Errors**: Ensure all dependencies are installed
- **Path Issues**: Check file paths and permissions
- **Memory Issues**: Large models may require significant memory
- **Version Compatibility**: Ensure scikit-learn versions are compatible

### Debugging Tips

- Add print statements to track execution flow
- Check file permissions and directory structure
- Verify model file integrity after saving
- Test with smaller datasets for development
