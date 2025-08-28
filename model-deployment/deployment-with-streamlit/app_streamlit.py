import streamlit as st
from save_load import load_model

model = load_model()

st.title(" Iris Flower Classifier")
st.write("Enter the flower measurements to predict its species.")

sepal_length = st.slider("Sepal Length", 4.0, 8.0, 5.1)
sepal_width = st.slider("Sepal Width", 2.0, 4.5, 3.5)
petal_length = st.slider("Petal Length", 1.0, 7.0, 1.4)
petal_width = st.slider("Petal Width", 0.1, 2.5, 0.2)

if st.button("Predict"):
    features = [[sepal_length, sepal_width, petal_length, petal_width]]
    prediction = model.predict(features)
    st.success(f" Prediction: {prediction[0]}")