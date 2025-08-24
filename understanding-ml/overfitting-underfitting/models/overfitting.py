import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error

def polynomial_regression_example():
    # Sample dataset
    X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
    y = np.array([1, 4, 9, 16, 25])  # Quadratic relationship (y = x^2)

    # Linear Regression (Underfitting case)
    linear_model = LinearRegression().fit(X, y)
    y_pred_linear = linear_model.predict(X)
    mse_linear = mean_squared_error(y, y_pred_linear)

    # Polynomial Regression (Overfitting case if degree too high)
    poly = PolynomialFeatures(degree=4)
    X_poly = poly.fit_transform(X)
    poly_model = LinearRegression().fit(X_poly, y)
    y_pred_poly = poly_model.predict(X_poly)
    mse_poly = mean_squared_error(y, y_pred_poly)

    return X, y, y_pred_linear, y_pred_poly, mse_linear, mse_poly