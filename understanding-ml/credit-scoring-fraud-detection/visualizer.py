import matplotlib.pyplot as plt

def visualize_anomalies(data):
    plt.figure(figsize=(10, 6))
    plt.scatter(
        data['transaction_amount'],
        data['transaction_frequency'],
        c=data['anomaly'],
        cmap='coolwarm',
        edgecolor='k',
        s=60
    )
    plt.title("Fraud Detection Using Isolation Forest")
    plt.xlabel("Transaction Amount")
    plt.ylabel("Transaction Frequency")
    plt.grid(True)
    plt.show()