# FastAPI Model Deployment

This directory contains a FastAPI-based deployment of the Iris flower classification model. FastAPI is a modern, high-performance web framework for building APIs with Python.

## Overview

FastAPI provides:
- High performance and speed
- Automatic API documentation
- Built-in data validation
- Type hints support
- Easy testing and debugging

## Files

- `app_fastapi.py` - Main FastAPI application
- `save_load.py` - Model loading utilities

## Installation

Install the required dependencies:

```bash
pip install fastapi uvicorn scikit-learn joblib
```

## Running the Application

1. **Start the server:**
   ```bash
   python app_fastapi.py
   ```

2. **Access the application:**
   - API endpoint: http://localhost:8000
   - Interactive documentation: http://localhost:8000/docs
   - Alternative documentation: http://localhost:8000/redoc

## API Usage

### Endpoint: POST /predict

**Request Body:**
```json
{
  "features": [5.1, 3.5, 1.4, 0.2]
}
```

**Response:**
```json
{
  "prediction": ["setosa"]
}
```

### Example with curl

```bash
curl -X POST "http://localhost:8000/predict" \
     -H "Content-Type: application/json" \
     -d '{"features": [5.1, 3.5, 1.4, 0.2]}'
```

### Example with Python requests

```python
import requests

url = "http://localhost:8000/predict"
data = {"features": [5.1, 3.5, 1.4, 0.2]}
response = requests.post(url, json=data)
prediction = response.json()["prediction"]
print(f"Prediction: {prediction}")
```

## Features

- **Automatic Validation**: Input data is automatically validated using Pydantic models
- **Type Safety**: Full type hints support for better development experience
- **API Documentation**: Automatic OpenAPI documentation generation
- **High Performance**: Built on top of Starlette and Pydantic for optimal performance

## Model Input

The model expects four features in the following order:
1. Sepal length (float)
2. Sepal width (float)
3. Petal length (float)
4. Petal width (float)

## Error Handling

The API includes built-in error handling for:
- Invalid input data
- Missing required fields
- Type validation errors

## Production Deployment

For production use, consider:
- Using a production ASGI server like Gunicorn with Uvicorn workers
- Adding authentication and rate limiting
- Implementing logging and monitoring
- Using environment variables for configuration

## Customization

To use this deployment with a different model:
1. Update the `Features` model in `app_fastapi.py`
2. Modify the prediction logic as needed
3. Update the input validation rules

## Troubleshooting

- **Port already in use**: Change the port in the `uvicorn.run()` call
- **Model not found**: Ensure the model file exists in the correct path
- **Import errors**: Verify all dependencies are installed correctly
