from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def train_model(X, y):
    model = RandomForestClassifier()
    model.fit(X, y)
    return model

def evaluate_model(model, X, y):
    predictions = model.predict(X)
    return accuracy_score(y, predictions)
