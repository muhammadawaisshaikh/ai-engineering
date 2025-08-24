import matplotlib.pyplot as plt
import numpy as np

def plot_decision_boundaries(models, X, y):
    h = .02  # step size
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                         np.arange(y_min, y_max, h))

    for name, model in models.items():
        plt.figure(figsize=(5, 4))
        Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
        Z = Z.reshape(xx.shape)
        plt.contourf(xx, yy, Z, cmap="gray", alpha=0.6)  # black/white
        plt.scatter(X[:, 0], X[:, 1], c=y, cmap="gray", edgecolors="k")
        plt.title(f"Decision Boundary: {name}")
        plt.show()

def plot_metrics_bar(results):
    metrics = ["Accuracy", "Precision", "Recall", "F1 Score"]
    models = list(results.keys())

    for metric in metrics:
        values = [results[model][metric] for model in models]
        plt.figure(figsize=(6, 4))
        plt.bar(models, values, color="black", alpha=0.7)
        plt.ylim(0, 1)
        plt.title(f"{metric} Comparison")
        plt.ylabel(metric)
        plt.show()