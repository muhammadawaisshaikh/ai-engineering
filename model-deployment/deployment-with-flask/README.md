# Flask Model Deployment

This directory contains a Flask-based deployment of the Iris flower classification model. Flask is a lightweight and flexible web framework for building web applications in Python.

## Overview

Flask provides:
- Simple and minimalistic design
- Easy to learn and use
- Flexible structure for small to medium applications
- Extensive ecosystem of extensions
- Great for prototyping and simple APIs

## Files

- `app_flask.py` - Main Flask application
- `save_load.py` - Model loading utilities

## Installation

Install the required dependencies:

```bash
pip install flask scikit-learn joblib
```

## Running the Application

1. **Start the server:**
   ```bash
   python app_flask.py
   ```

2. **Access the application:**
   - API endpoint: http://localhost:5000
   - The server runs in debug mode by default

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
curl -X POST "http://localhost:5000/predict" \
     -H "Content-Type: application/json" \
     -d '{"features": [5.1, 3.5, 1.4, 0.2]}'
```

### Example with Python requests

```python
import requests

url = "http://localhost:5000/predict"
data = {"features": [5.1, 3.5, 1.4, 0.2]}
response = requests.post(url, json=data)
prediction = response.json()["prediction"]
print(f"Prediction: {prediction}")
```

## Features

- **Simple REST API**: Clean and straightforward endpoint design
- **JSON Support**: Built-in JSON request and response handling
- **Error Handling**: Basic error handling for malformed requests
- **Debug Mode**: Development-friendly with detailed error messages

## Model Input

The model expects four features in the following order:
1. Sepal length (float)
2. Sepal width (float)
3. Petal length (float)
4. Petal width (float)

## Application Structure

The Flask app follows a simple structure:
- Single route for predictions
- JSON input validation
- Direct model inference
- JSON response formatting

## Development vs Production

### Development (Current Setup)
- Debug mode enabled
- Single-threaded server
- Detailed error messages
- Auto-reload on code changes

### Production Considerations
- Disable debug mode
- Use production WSGI server (Gunicorn, uWSGI)
- Add proper logging
- Implement security measures
- Add input validation and sanitization

## Customization

To adapt this deployment for other models:

1. **Update Input Format**: Modify the expected JSON structure in the route
2. **Add Validation**: Implement input validation for your specific features
3. **Extend Routes**: Add additional endpoints for different model operations
4. **Error Handling**: Implement comprehensive error handling for your use case

## Adding More Functionality

Common extensions you might want to add:

```python
# Add health check endpoint
@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "healthy"})

# Add model information endpoint
@app.route("/model-info", methods=["GET"])
def model_info():
    return jsonify({
        "model_type": "Iris Classifier",
        "features": ["sepal_length", "sepal_width", "petal_length", "petal_width"]
    })
```

## Testing

Test the API using tools like:
- **Postman**: GUI-based API testing
- **curl**: Command-line testing
- **Python requests**: Programmatic testing
- **Flask test client**: Unit testing

## Troubleshooting

- **Port conflicts**: Change the port in `app.run(port=5001)`
- **Import errors**: Ensure all dependencies are installed
- **Model loading issues**: Check the model file path in `save_load.py`
- **JSON parsing errors**: Verify the request format matches the expected structure

## Security Notes

The current implementation is basic and suitable for development. For production use, consider:
- Input sanitization and validation
- Rate limiting
- Authentication and authorization
- HTTPS enforcement
- Request size limits
