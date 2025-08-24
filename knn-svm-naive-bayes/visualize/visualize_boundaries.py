import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

def plot_decision_boundary(model, X, y, title):
    """
    Plots the decision boundary of a trained classifier.
    Args:
        model: Trained ML model with .predict method
        X: Feature matrix (2D only for plotting)
        y: Target labels
        title: Title of the plot
    """

    # Define black & white colormap
    cmap_background = ListedColormap(["#ffffff", "#000000"])  
    cmap_points = ListedColormap(["#aaaaaa", "#222222"])  

    # Step 1: Create a mesh grid covering data points
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.02),
                         np.arange(y_min, y_max, 0.02))

    # Step 2: Predict class for each point in the grid
    Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)

    # Step 3: Plot decision surface
    plt.figure(figsize=(6, 5))
    plt.contourf(xx, yy, Z, cmap=cmap_background, alpha=0.8)

    # Step 4: Plot original points
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap=cmap_points, edgecolor="k", s=50)
    plt.title(title)
    plt.xlabel("Feature 1")
    plt.ylabel("Feature 2")
    plt.show()