import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

def load_dataset(n_samples=1000, n_features=20, n_informative=15, n_redundant=5, random_state=42):
    """
    Load a synthetic dataset for ML training and tuning examples.
    
    Parameters:
    -----------
    n_samples : int, default=1000
        Number of samples to generate
    n_features : int, default=20
        Total number of features
    n_informative : int, default=15
        Number of informative features
    n_redundant : int, default=5
        Number of redundant features
    random_state : int, default=42
        Random state for reproducibility
        
    Returns:
    --------
    X : array-like of shape (n_samples, n_features)
        The generated samples
    y : array-like of shape (n_samples,)
        The integer labels for class membership
    """
    # Generate synthetic classification dataset
    X, y = make_classification(
        n_samples=n_samples,
        n_features=n_features,
        n_informative=n_informative,
        n_redundant=n_redundant,
        n_classes=2,
        random_state=random_state
    )
    
    print(f"Dataset loaded: {X.shape[0]} samples, {X.shape[1]} features")
    print(f"Class distribution: {np.bincount(y)}")
    
    return X, y

def load_regression_dataset(n_samples=1000, n_features=10, noise=0.1, random_state=42):
    """
    Load a synthetic regression dataset.
    
    Parameters:
    -----------
    n_samples : int, default=1000
        Number of samples to generate
    n_features : int, default=10
        Number of features
    noise : float, default=0.1
        Standard deviation of the gaussian noise
    random_state : int, default=42
        Random state for reproducibility
        
    Returns:
    --------
    X : array-like of shape (n_samples, n_features)
        The generated samples
    y : array-like of shape (n_samples,)
        The target values
    """
    from sklearn.datasets import make_regression
    
    X, y = make_regression(
        n_samples=n_samples,
        n_features=n_features,
        noise=noise,
        random_state=random_state
    )
    
    print(f"Regression dataset loaded: {X.shape[0]} samples, {X.shape[1]} features")
    print(f"Target range: {y.min():.2f} to {y.max():.2f}")
    
    return X, y
