from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB

def train_models(X_train, y_train):
    models = {
        "KNN": KNeighborsClassifier(n_neighbors=5),
        "SVM": SVC(kernel="linear", probability=True),
        "Naive Bayes": GaussianNB()
    }
    for name, model in models.items():
        model.fit(X_train, y_train)
    return models