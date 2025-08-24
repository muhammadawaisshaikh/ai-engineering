import matplotlib.pyplot as plt

def plot_overfitting(X, y, y_pred_linear, y_pred_poly):
    plt.scatter(X, y, color="black", label="True Data")
    plt.plot(X, y_pred_linear, label="Linear Model (Underfitting)", color="blue")
    plt.plot(X, y_pred_poly, label="Polynomial Model (Potential Overfitting)", color="red")
    plt.xlabel("X")
    plt.ylabel("y")
    plt.legend()
    plt.title("Overfitting vs Underfitting")
    plt.show()