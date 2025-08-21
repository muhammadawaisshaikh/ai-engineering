from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

def train_weighted_model(X_train, y_train, X_test, y_test):
    """Train a logistic regression model with balanced class weights."""
    model = LogisticRegression(class_weight="balanced", random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    print("Classification Report with Class Weights:\n")
    print(classification_report(y_test, y_pred))
