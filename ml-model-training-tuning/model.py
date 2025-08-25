from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC

def build_model(model_type='logistic', **kwargs):
    """
    Build a machine learning model based on the specified type.
    
    Parameters:
    -----------
    model_type : str, default='logistic'
        Type of model to build. Options: 'logistic', 'tree', 'forest', 'svm'
    **kwargs : dict
        Additional parameters to pass to the model constructor
        
    Returns:
    --------
    model : sklearn estimator
        The configured model
    """
    if model_type == 'logistic':
        default_params = {'max_iter': 1000, 'random_state': 42}
        default_params.update(kwargs)
        return LogisticRegression(**default_params)
    
    elif model_type == 'tree':
        default_params = {'random_state': 42, 'max_depth': 5}
        default_params.update(kwargs)
        return DecisionTreeClassifier(**default_params)
    
    elif model_type == 'forest':
        default_params = {'n_estimators': 100, 'random_state': 42, 'max_depth': 10}
        default_params.update(kwargs)
        return RandomForestClassifier(**default_params)
    
    elif model_type == 'svm':
        default_params = {'random_state': 42, 'probability': True}
        default_params.update(kwargs)
        return SVC(**default_params)
    
    else:
        raise ValueError(f"Unknown model type: {model_type}. Available types: logistic, tree, forest, svm")

def get_model_params(model_type='logistic'):
    """
    Get default hyperparameter grid for a specific model type.
    
    Parameters:
    -----------
    model_type : str, default='logistic'
        Type of model to get parameters for
        
    Returns:
    --------
    param_grid : dict
        Dictionary of parameter names and lists of values to try
    """
    if model_type == 'logistic':
        return {
            'C': [0.001, 0.01, 0.1, 1, 10, 100],
            'penalty': ['l1', 'l2'],
            'solver': ['liblinear', 'saga']
        }
    
    elif model_type == 'tree':
        return {
            'max_depth': [3, 5, 7, 10, None],
            'min_samples_split': [2, 5, 10],
            'min_samples_leaf': [1, 2, 4]
        }
    
    elif model_type == 'forest':
        return {
            'n_estimators': [50, 100, 200],
            'max_depth': [5, 10, 15, None],
            'min_samples_split': [2, 5, 10]
        }
    
    elif model_type == 'svm':
        return {
            'C': [0.1, 1, 10, 100],
            'gamma': ['scale', 'auto', 0.001, 0.01, 0.1],
            'kernel': ['rbf', 'linear']
        }
    
    else:
        raise ValueError(f"Unknown model type: {model_type}")
