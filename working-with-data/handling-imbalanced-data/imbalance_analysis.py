import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
from sklearn.datasets import make_classification

def load_imbalanced_data():
    """Generate a synthetic imbalanced dataset for demonstration."""
    X, y = make_classification(n_classes=2, 
                               class_sep=2, 
                               weights=[0.9, 0.1], 
                               n_informative=3, 
                               n_redundant=1, 
                               flip_y=0, 
                               n_features=5, 
                               n_clusters_per_class=1, 
                               n_samples=1000, 
                               random_state=42)
    return X, y

def analyze_distribution(y):
    """Check the class balance."""
    counter = Counter(y)
    print("Class distribution:", counter)
    
    # Plot the imbalance
    plt.bar(counter.keys(), counter.values(), color=['blue', 'red'])
    plt.title("Class Distribution")
    plt.xlabel("Class")
    plt.ylabel("Frequency")
    plt.show()