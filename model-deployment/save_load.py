import joblib
import os

def save_model(model, path="./models/iris_model.pkl"):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    joblib.dump(model, path)
    print(f" Model saved at {path}")

def load_model(path="./models/iris_model.pkl"):
    model = joblib.load(path)
    print(f" Model loaded from {path}")
    return model