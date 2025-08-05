from data_generator import generate_transaction_data
from anomaly_detector import detect_anomalies
from visualizer import visualize_anomalies

def run_pipeline():
    # Step 1: Generate synthetic transaction data
    transaction_data = generate_transaction_data()

    # Step 2: Detect fraud using Isolation Forest
    results, model = detect_anomalies(transaction_data)

    # Step 3: Visualize the anomalies
    visualize_anomalies(results)

    # Print some of the fraud cases
    fraud_cases = results[results['anomaly'] == -1]
    print("Sample Fraudulent Transactions:\n", fraud_cases.head())

if __name__ == "__main__":
    run_pipeline()