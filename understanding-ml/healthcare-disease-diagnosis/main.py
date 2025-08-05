from data_loader import load_healthcare_data
from diagnosis_model import DiseaseDiagnosisModel

def run_diagnosis_pipeline():
    X_train, X_test, y_train, y_test = load_healthcare_data()
    
    model = DiseaseDiagnosisModel()
    model.train(X_train, y_train)
    
    accuracy = model.evaluate(X_test, y_test)
    print(f"Diagnosis Accuracy: {accuracy * 100:.2f}%")

if __name__ == "__main__":
    run_diagnosis_pipeline()