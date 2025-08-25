from sklearn.tree import DecisionTreeClassifier
from model import build_model
from trainer import cross_validate
from utils import average_results
import matplotlib.pyplot as plt

def compare_models(X, y):
    """
    Compare bias-variance behavior of simple vs complex models with plots.
    """
    # Logistic Regression
    def create_logistic_model():
        return build_model('logistic')
    
    logreg_results = cross_validate(create_logistic_model, X, y, folds=5)
    avg_logreg = average_results(logreg_results)

    # Decision Tree
    def create_tree_model():
        return DecisionTreeClassifier(max_depth=None, random_state=42)
    
    tree_results = cross_validate(create_tree_model, X, y, folds=5)
    avg_tree = average_results(tree_results)

    # Plot comparison
    logreg_acc = [r["accuracy"] for r in logreg_results]
    tree_acc = [r["accuracy"] for r in tree_results]

    plt.figure(figsize=(10, 6))
    plt.plot(range(1, 6), logreg_acc, marker="o", label="Logistic Regression", linewidth=2, markersize=8)
    plt.plot(range(1, 6), tree_acc, marker="s", label="Decision Tree", linewidth=2, markersize=8)
    plt.xlabel("Fold")
    plt.ylabel("Accuracy")
    plt.title("Bias vs Variance in Practice")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.xticks(range(1, 6))
    plt.tight_layout()
    plt.show()

    return avg_logreg, avg_tree