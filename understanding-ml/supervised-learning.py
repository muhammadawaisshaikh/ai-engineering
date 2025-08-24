from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pandas as pd

# Sample dataset - increased size to avoid evaluation issues
data = {
    'area': [1000, 1200, 1500, 1800, 2000, 2200, 2400, 2600, 2800, 3000, 3200, 3500],
    'price': [300000, 350000, 400000, 450000, 500000, 550000, 600000, 650000, 700000, 750000, 800000, 850000]
}

df = pd.DataFrame(data)

# Features and labels
X = df[['area']]
y = df['price']

# Split and train - adjusted test size for better evaluation
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)

# Prediction with proper feature names
area_for_prediction = pd.DataFrame({'area': [2000]})
predicted_price = model.predict(area_for_prediction)
print(f"Predicted price: ${predicted_price[0]:.2f}")

# Show model performance
train_score = model.score(X_train, y_train)
test_score = model.score(X_test, y_test)
print(f"Training R² score: {train_score:.4f}")
print(f"Testing R² score: {test_score:.4f}")

# Show the relationship
print(f"\nModel equation: Price = ${model.intercept_:.2f} + ${model.coef_[0]:.2f} × Area")
print(f"For 2000 sq ft: ${model.intercept_:.2f} + ${model.coef_[0]:.2f} × 2000 = ${predicted_price[0]:.2f}")

# Show dataset info
print(f"\nDataset info:")
print(f"Total samples: {len(df)}")
print(f"Training samples: {len(X_train)}")
print(f"Testing samples: {len(X_test)}")