from sklearn.svm import SVC

class SVMModel:
    def __init__(self, kernel='linear', C=1.0):
        self.model = SVC(kernel=kernel, C=C)

    def train(self, X_train, y_train):
        self.model.fit(X_train, y_train)

    def predict(self, X_test):
        return self.model.predict(X_test)