
from sklearn.metrics import r2_score, mean_absolute_error

class Evaluation:
    def __init__(self, model, X_test, y_test):
        self.model = model
        self.X_test = X_test
        self.y_test = y_test

    def evaluate(self):
        predictions = self.model.predict(self.X_test)
        r2 = r2_score(self.y_test, predictions)
        mae = mean_absolute_error(self.y_test, predictions)
        print(f" R² Score: {r2:.2f}")
        print(f" MAE: {mae:.2f}")
