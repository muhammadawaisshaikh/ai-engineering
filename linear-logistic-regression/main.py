from utils.data_loader import load_regression_data, load_classification_data
from models.linear_logistic import train_linear_regression, train_logistic_regression

if __name__ == "__main__":
    # Linear Regression
    X_train, X_test, y_train, y_test = load_regression_data()
    mse = train_linear_regression(X_train, X_test, y_train, y_test)
    print(f"Linear Regression MSE: {mse:.2f}")

    # Logistic Regression
    X_train, X_test, y_train, y_test = load_classification_data()
    acc = train_logistic_regression(X_train, X_test, y_train, y_test)
    print(f"Logistic Regression Accuracy: {acc:.2f}")