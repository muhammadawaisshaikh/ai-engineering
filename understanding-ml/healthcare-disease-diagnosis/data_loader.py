from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split

def load_healthcare_data(test_size=0.2, random_state=42):
    data = load_breast_cancer()
    X = data.data
    y = data.target
    return train_test_split(X, y, test_size=test_size, random_state=random_state)