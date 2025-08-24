from models.overfitting import polynomial_regression_example
from utils.visualization import plot_overfitting

if __name__ == "__main__":
    X, y, y_pred_linear, y_pred_poly, mse_linear, mse_poly = polynomial_regression_example()

    print(f"Linear Model MSE: {mse_linear:.2f}")
    print(f"Polynomial Model MSE: {mse_poly:.2f}")

    plot_overfitting(X, y, y_pred_linear, y_pred_poly)