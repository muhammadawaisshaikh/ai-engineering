from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from knn_model import KNNModel
from svm_model import SVMModel
from naive_bayes_model import NaiveBayesModel

# Load dataset
iris = load_iris()
X, y = iris.data, iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train and evaluate KNN
knn = KNNModel(n_neighbors=3)
knn.train(X_train, y_train)
knn_preds = knn.predict(X_test)
print("KNN Accuracy:", accuracy_score(y_test, knn_preds))

# Train and evaluate SVM
svm = SVMModel(kernel='linear')
svm.train(X_train, y_train)
svm_preds = svm.predict(X_test)
print("SVM Accuracy:", accuracy_score(y_test, svm_preds))

# Train and evaluate Naive Bayes
nb = NaiveBayesModel()
nb.train(X_train, y_train)
nb_preds = nb.predict(X_test)
print("Naive Bayes Accuracy:", accuracy_score(y_test, nb_preds))
