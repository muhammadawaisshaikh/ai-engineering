from sklearn.ensemble import IsolationForest

def detect_anomalies(data, contamination_rate=0.02):
    model = IsolationForest(contamination=contamination_rate, random_state=42)
    model.fit(data)

    data['anomaly'] = model.predict(data)  # -1 = anomaly, 1 = normal
    return data, model