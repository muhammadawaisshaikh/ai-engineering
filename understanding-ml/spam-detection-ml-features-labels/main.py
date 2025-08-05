from data_loader import generate_sample_emails
from feature_engineering import extract_features
from model import train_model, evaluate_model

def main():
    df = generate_sample_emails()
    X, y = extract_features(df)
    model = train_model(X, y)
    acc = evaluate_model(model, X, y)
    print(f"Spam Detection Accuracy: {acc * 100:.2f}%")

if __name__ == "__main__":
    main()
