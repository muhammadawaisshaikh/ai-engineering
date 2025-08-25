from sklearn.model_selection import KFold
from utils import calculate_classification_metrics
import matplotlib.pyplot as plt
import numpy as np

def cross_validate(model_builder, X, y, folds=5):
    """
    Performs K-Fold Cross Validation and plots fold results.
    """
    kf = KFold(n_splits=folds, shuffle=True, random_state=42)
    results = []

    for fold, (train_idx, test_idx) in enumerate(kf.split(X)):
        print(f"\nFold {fold+1}/{folds}")
        X_train, X_test = X[train_idx], X[test_idx]
        y_train, y_test = y[train_idx], y[test_idx]

        model = model_builder()
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

        metrics = calculate_classification_metrics(y_test, y_pred)
        print(f"Metrics: {metrics}")
        results.append(metrics)

    # Plotting accuracy across folds
    accuracies = [r["accuracy"] for r in results]
    plt.figure(figsize=(8, 6))
    plt.plot(range(1, folds+1), accuracies, marker="o", linewidth=2, markersize=8)
    plt.xlabel("Fold")
    plt.ylabel("Accuracy")
    plt.title("Cross-Validation Accuracies")
    plt.grid(True, alpha=0.3)
    plt.xticks(range(1, folds+1))
    plt.tight_layout()
    plt.show()

    return results