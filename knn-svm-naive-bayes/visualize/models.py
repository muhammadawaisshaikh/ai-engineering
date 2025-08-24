from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from visualize_boundaries import plot_decision_boundary

def knn_demo():
    # Generate simple 2D dataset
    X, y = make_classification(n_samples=200, n_features=2,
                               n_redundant=0, n_informative=2,
                               n_clusters_per_class=1, random_state=42)

    # Train KNN
    model = KNeighborsClassifier(n_neighbors=5)
    model.fit(X, y)

    # Plot decision boundary
    plot_decision_boundary(model, X, y, "KNN Decision Boundary (k=5)")

def svm_demo():
    X, y = make_classification(n_samples=200, n_features=2,
                               n_redundant=0, n_informative=2,
                               n_clusters_per_class=1, random_state=42)

    # Train SVM with linear kernel
    model = SVC(kernel="linear")
    model.fit(X, y)

    # Plot decision boundary
    plot_decision_boundary(model, X, y, "SVM Decision Boundary (Linear)")

def naive_bayes_demo():
    X, y = make_classification(n_samples=200, n_features=2,
                               n_redundant=0, n_informative=2,
                               n_clusters_per_class=1, random_state=42)

    # Train Naive Bayes
    model = GaussianNB()
    model.fit(X, y)

    # Plot decision boundary
    plot_decision_boundary(model, X, y, "Naive Bayes Decision Boundary")