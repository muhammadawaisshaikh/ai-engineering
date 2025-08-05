# simple regression model to predict house prices based on size using scikit-learn
from sklearn.linear_model import LinearRegression
import numpy as np

# Dataset: House size (sq ft) vs Price (k$)
X = np.array([[1000], [1500], [2000], [2500], [3000]])
y = np.array([150, 200, 250, 300, 350])

# Train the model
model = LinearRegression()
model.fit(X, y)

# Predict price of a 2200 sq ft house
predicted_price = model.predict([[2200]])
print(f"Predicted Price: ${predicted_price[0]*1000:.2f}")
