# Credit Scoring and Fraud Detection with Isolation Forest

## Overview
This project demonstrates how to build a fraud detection system for financial transactions using machine learning. It's designed to help banks and fintech platforms identify suspicious transactions that could indicate fraudulent activity. The system uses synthetic data to simulate real-world scenarios and showcases the power of unsupervised anomaly detection.

## What This Project Does
The system analyzes transaction patterns across three key dimensions to identify unusual behavior:

- **Transaction Amount**: Monitors spending patterns and flags transactions that are significantly higher than normal
- **Transaction Frequency**: Tracks how often a user makes transactions and detects unusual activity spikes
- **Location Score**: Identifies transactions that occur far from a user's typical geographic patterns

## How It Works
The fraud detection pipeline follows these steps:

1. **Data Generation**: Creates realistic synthetic transaction data with both normal patterns and intentional anomalies
2. **Anomaly Detection**: Uses Isolation Forest algorithm to identify outliers in the transaction data
3. **Visualization**: Provides clear visual representation of detected fraud cases
4. **Results Analysis**: Outputs detailed information about suspicious transactions

## Technical Implementation

### Core Components
- **`main.py`**: Orchestrates the entire fraud detection pipeline
- **`data_generator.py`**: Creates synthetic transaction data with controlled anomalies
- **`anomaly_detector.py`**: Implements the Isolation Forest algorithm for outlier detection
- **`visualizer.py`**: Generates scatter plots to visualize fraud detection results

### Machine Learning Model
The project uses **Isolation Forest**, an unsupervised anomaly detection algorithm that:
- Works without labeled training data
- Automatically identifies outliers based on data isolation patterns
- Is particularly effective for financial fraud detection
- Configurable contamination rate (default: 2% of transactions flagged as suspicious)

## Getting Started

### Prerequisites
- Python 3.7+
- Required packages: pandas, numpy, scikit-learn, matplotlib

### Running the Project
Simply execute the main script:
```bash
python main.py
```

This will:
- Generate synthetic transaction data
- Run the fraud detection algorithm
- Display visual results
- Print sample fraudulent transactions

## Use Cases
This system is ideal for:
- **Banks**: Monitoring customer transaction patterns
- **E-commerce**: Detecting suspicious purchase behavior
- **Payment Processors**: Identifying fraudulent transactions in real-time
- **Financial Analysts**: Understanding anomaly detection techniques

## Customization
You can easily modify the system by:
- Adjusting the contamination rate in `anomaly_detector.py`
- Adding new features to the transaction data
- Implementing different anomaly detection algorithms
- Customizing the visualization outputs

## Why Isolation Forest?
Isolation Forest is particularly well-suited for financial fraud detection because it:
- Requires minimal parameter tuning
- Handles high-dimensional data efficiently
- Provides interpretable results
- Works well with real-time data streams