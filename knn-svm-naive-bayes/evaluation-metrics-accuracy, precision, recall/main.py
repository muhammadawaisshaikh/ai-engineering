from data_loader import load_dataset
from models_knn_svm_nb import train_models
from evaluation import evaluate_models
from visualization import plot_decision_boundaries, plot_metrics_bar

def main():
    # Step 1: Load dataset
    X_train, X_test, y_train, y_test, X, y = load_dataset()

    # Step 2: Train Models (KNN, SVM, Naive Bayes)
    models = train_models(X_train, y_train)

    # Step 3: Evaluate Models
    results = evaluate_models(models, X_test, y_test)

    # Step 4: Visualize Decision Boundaries
    plot_decision_boundaries(models, X, y)

    # Step 5: Visualize Metric Comparisons
    plot_metrics_bar(results)

if __name__ == "__main__":
    main()