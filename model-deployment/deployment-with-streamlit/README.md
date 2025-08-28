# Streamlit Model Deployment

This directory contains a Streamlit-based deployment of the Iris flower classification model. Streamlit is an open-source framework for creating interactive web applications for machine learning and data science projects.

## Overview

Streamlit provides:
- Rapid development of interactive web apps
- Built-in widgets for user input
- Automatic layout management
- Real-time updates and interactions
- Python-native development experience

## Files

- `app_streamlit.py` - Main Streamlit application
- `save_load.py` - Model loading utilities

## Installation

Install the required dependencies:

```bash
pip install streamlit scikit-learn joblib
```

## Running the Application

1. **Start the Streamlit app:**
   ```bash
   streamlit run app_streamlit.py
   ```

2. **Access the application:**
   - The app will automatically open in your default web browser
   - Default URL: http://localhost:8501
   - Streamlit will show the local URL in the terminal

## Application Features

### Interactive Interface

The Streamlit app provides:
- **Title and Description**: Clear explanation of the application
- **Input Sliders**: Interactive sliders for each flower measurement
- **Predict Button**: Button to trigger model prediction
- **Results Display**: Success message showing the prediction

### Input Controls

Four interactive sliders for flower measurements:
- **Sepal Length**: Range 4.0 to 8.0 cm (default: 5.1)
- **Sepal Width**: Range 2.0 to 4.5 cm (default: 3.5)
- **Petal Length**: Range 1.0 to 7.0 cm (default: 1.4)
- **Petal Width**: Range 0.1 to 2.5 cm (default: 0.2)

### Model Prediction

When you click the "Predict" button:
1. The app collects values from all sliders
2. Formats the input for the model
3. Runs the prediction
4. Displays the result in a success message

## Usage Instructions

1. **Adjust Measurements**: Use the sliders to set the flower measurements
2. **Make Prediction**: Click the "Predict" button
3. **View Results**: See the predicted flower species
4. **Experiment**: Try different combinations of measurements

## Model Information

The underlying model is trained on the classic Iris dataset and can predict three species:
- **Setosa**: Characterized by small petals
- **Versicolor**: Medium-sized petals
- **Virginica**: Large petals

## Customization Options

### Adding More Input Types

You can extend the app with additional input methods:

```python
# Add text input for custom values
custom_input = st.text_input("Enter custom measurements (comma-separated)")

# Add file upload for batch predictions
uploaded_file = st.file_uploader("Upload CSV file with measurements")

# Add selectbox for model selection
model_choice = st.selectbox("Choose Model", ["Iris Classifier", "Alternative Model"])
```

### Enhancing the Interface

```python
# Add sidebar for additional options
with st.sidebar:
    st.header("Model Settings")
    confidence_threshold = st.slider("Confidence Threshold", 0.0, 1.0, 0.5)
    
# Add multiple columns for better layout
col1, col2 = st.columns(2)
with col1:
    st.write("Sepal Measurements")
with col2:
    st.write("Petal Measurements")
```

### Adding Visualizations

```python
# Show prediction confidence
import matplotlib.pyplot as plt
probabilities = model.predict_proba(features)[0]
st.bar_chart(probabilities)

# Display feature importance
feature_importance = pd.DataFrame({
    'Feature': ['Sepal Length', 'Sepal Width', 'Petal Length', 'Petal Width'],
    'Value': features[0]
})
st.bar_chart(feature_importance.set_index('Feature'))
```

## Development Workflow

1. **Edit the app**: Modify `app_streamlit.py`
2. **Save changes**: Streamlit automatically reloads the app
3. **Test interactions**: Use the interface to test your changes
4. **Iterate**: Make improvements based on testing

## Deployment Considerations

### Local Development
- Runs on localhost
- Automatic reloading on code changes
- Debug information in terminal

### Production Deployment
- Deploy to cloud platforms (Heroku, AWS, Google Cloud)
- Use Streamlit Cloud for easy deployment
- Consider containerization with Docker
- Set up proper logging and monitoring

## Troubleshooting

### Common Issues

- **Port conflicts**: Change the port with `streamlit run app_streamlit.py --server.port 8502`
- **Model loading errors**: Check the model file path in `save_load.py`
- **Import errors**: Ensure all dependencies are installed
- **Slider range issues**: Adjust the min/max values in the slider definitions

### Performance Tips

- **Caching**: Use `@st.cache_data` for expensive operations
- **Session state**: Use `st.session_state` for persistent data
- **Efficient updates**: Minimize unnecessary re-computations

## Extending the Application

### Adding New Models

To support different models:
1. Update the model loading logic
2. Modify input requirements
3. Adjust the prediction display
4. Update the feature descriptions

### Adding Data Validation

```python
# Validate input ranges
if not (4.0 <= sepal_length <= 8.0):
    st.error("Sepal length must be between 4.0 and 8.0 cm")
    return

# Check for reasonable combinations
if petal_length < petal_width:
    st.warning("Petal length should typically be greater than petal width")
```

### Adding Export Functionality

```python
# Export predictions to CSV
if st.button("Export Results"):
    results_df = pd.DataFrame({
        'Sepal Length': [sepal_length],
        'Sepal Width': [sepal_width],
        'Petal Length': [petal_length],
        'Petal Width': [petal_width],
        'Prediction': [prediction[0]]
    })
    csv = results_df.to_csv(index=False)
    st.download_button("Download CSV", csv, "iris_prediction.csv")
```

## Best Practices

- **User Experience**: Make the interface intuitive and responsive
- **Error Handling**: Provide clear error messages for invalid inputs
- **Documentation**: Include helpful text explaining how to use the app
- **Responsiveness**: Design for different screen sizes
- **Accessibility**: Ensure the app is usable by people with disabilities
