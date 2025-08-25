from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
import matplotlib.pyplot as plt
import numpy as np

def grid_search(model, param_grid, X, y, cv=5):
    grid = GridSearchCV(model, param_grid, cv=cv, scoring="accuracy", return_train_score=True)
    grid.fit(X, y)

    # Plot results
    scores = grid.cv_results_["mean_test_score"]
    
    # Handle different parameter types for plotting
    if "C" in param_grid:
        params = [p["C"] for p in grid.cv_results_["params"]]
        param_name = "C (Regularization Strength)"
        use_log_scale = True
    else:
        # Use first parameter for plotting
        first_param = list(param_grid.keys())[0]
        params = [p[first_param] for p in grid.cv_results_["params"]]
        param_name = first_param
        use_log_scale = False
    
    plt.figure(figsize=(8, 6))
    plt.plot(params, scores, marker="o", linewidth=2, markersize=8)
    if use_log_scale:
        plt.xscale("log")
    plt.xlabel(param_name)
    plt.ylabel("Accuracy")
    plt.title("Grid Search Results")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

    return grid.best_params_, grid.best_score_

def random_search(model, param_dist, X, y, cv=5, n_iter=10):
    random = RandomizedSearchCV(model, param_dist, cv=cv, n_iter=n_iter, scoring="accuracy", random_state=42, return_train_score=True)
    random.fit(X, y)

    # Plot results
    scores = random.cv_results_["mean_test_score"]
    
    # Handle different parameter types for plotting
    if "C" in param_dist:
        params = [p["C"] for p in random.cv_results_["params"]]
        param_name = "C (Regularization Strength)"
        use_log_scale = True
    else:
        # Use first parameter for plotting
        first_param = list(param_dist.keys())[0]
        params = [p[first_param] for p in random.cv_results_["params"]]
        param_name = first_param
        use_log_scale = False
    
    plt.figure(figsize=(8, 6))
    plt.scatter(params, scores, color="red", s=100, alpha=0.7)
    if use_log_scale:
        plt.xscale("log")
    plt.xlabel(param_name)
    plt.ylabel("Accuracy")
    plt.title("Random Search Results")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

    return random.best_params_, random.best_score_