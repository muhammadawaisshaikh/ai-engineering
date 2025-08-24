from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

def load_dataset():
    # Generate synthetic 2D dataset for visualization
    X, y = make_classification(
        n_samples=300, n_features=2, n_classes=2,
        n_informative=2, n_redundant=0, random_state=42
    )
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42
    )
    return X_train, X_test, y_train, y_test, X, y