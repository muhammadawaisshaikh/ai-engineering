from train_model import train_model
from save_load import save_model, load_model

if __name__ == "__main__":
    # Train and save
    model = train_model()
    save_model(model)

    # Load and test
    loaded_model = load_model()
    sample_input = [[5.1, 3.5, 1.4, 0.2]]
    prediction = loaded_model.predict(sample_input)
    print(f"Prediction for {sample_input}: {prediction}")