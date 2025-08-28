# Model Deployment Examples

This directory contains practical examples of deploying machine learning models using different frameworks and approaches. Each subdirectory demonstrates a specific deployment method with complete working code.

## Project Structure

```
model-deployment/
├── deployment-with-fastapi/     # FastAPI web service deployment
├── deployment-with-flask/       # Flask web service deployment  
├── deployment-with-streamlit/   # Streamlit interactive web app
├── models/                      # Trained model files
├── main.py                     # Main training and testing script
├── train_model.py              # Model training script
└── save_load.py                # Model persistence utilities
```

## Overview

This project demonstrates how to:
- Train a simple machine learning model (Iris flower classifier)
- Save and load trained models using joblib
- Deploy models through different web frameworks
- Create interactive web applications for model inference

## Getting Started

1. **Install Dependencies**
   ```bash
   pip install scikit-learn joblib streamlit fastapi uvicorn flask
   ```

2. **Train the Model**
   ```bash
   python main.py
   ```

3. **Deploy Using Your Preferred Method**
   - **FastAPI**: `cd deployment-with-fastapi && python app_fastapi.py`
   - **Flask**: `cd deployment-with-flask && python app_flask.py`
   - **Streamlit**: `cd deployment-with-streamlit && streamlit run app_streamlit.py`

## Model Details

The example model is an Iris flower classifier trained on the classic Iris dataset. It predicts flower species based on four features:
- Sepal length
- Sepal width  
- Petal length
- Petal width

## Deployment Options

### FastAPI Deployment
High-performance, modern web framework with automatic API documentation. Ideal for production services requiring high throughput.

### Flask Deployment
Lightweight and flexible web framework. Great for simple REST APIs and quick prototypes.

### Streamlit Deployment
Interactive web application framework. Perfect for creating user-friendly interfaces where users can input data and see predictions.

## Key Features

- **Model Persistence**: Save and load trained models using joblib
- **Multiple Deployment Options**: Choose the framework that best fits your needs
- **Production Ready**: Includes proper error handling and input validation
- **Easy to Extend**: Simple structure makes it easy to adapt for other models

## Usage Examples

Each deployment method includes:
- Complete working code
- Input validation and error handling
- Clear documentation
- Ready-to-run examples

## Requirements

- Python 3.7+
- scikit-learn
- joblib
- FastAPI (for FastAPI deployment)
- Flask (for Flask deployment)
- Streamlit (for Streamlit deployment)
- uvicorn (for FastAPI server)

## Contributing

Feel free to add new deployment methods or improve existing ones. Each deployment should include:
- Working application code
- Clear documentation
- Example usage
- Requirements specification
