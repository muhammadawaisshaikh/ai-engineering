from data_loader import load_dataset
from model import build_model
from trainer import cross_validate
from utils import average_results
from tuner import grid_search, random_search
from bias_variance import compare_models
from pipeline_demo import pipeline_example

if __name__ == "__main__":
    X, y = load_dataset()

    print("\n=== Cross Validation Example ===")
    # Create a model builder function that returns a new model instance
    def create_logistic_model():
        return build_model('logistic')
    
    results = cross_validate(create_logistic_model, X, y, folds=5)
    avg_metrics = average_results(results)
    print("Average CV Results:", avg_metrics)

    print("\n=== Hyperparameter Tuning ===")
    from sklearn.linear_model import LogisticRegression
    model = LogisticRegression(max_iter=200)
    best_params, best_score = grid_search(model, {"C":[0.01,0.1,1,10]}, X, y)
    print("Grid Search:", best_params, best_score)
    best_params, best_score = random_search(model, {"C":[0.001,0.01,0.1,1,10,100]}, X, y, n_iter=4)
    print("Random Search:", best_params, best_score)

    print("\n=== Bias-Variance Tradeoff ===")
    avg_logreg, avg_tree = compare_models(X, y)
    print("Logistic Regression Avg:", avg_logreg)
    print("Decision Tree Avg:", avg_tree)

    print("\n=== Pipeline Example ===")
    avg_score = pipeline_example(X, y)
    print("Pipeline Avg Score:", avg_score)