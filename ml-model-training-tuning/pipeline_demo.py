from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt
import numpy as np

def pipeline_example(X, y):
    pipe = Pipeline([
        ("scaler", StandardScaler()),
        ("classifier", LogisticRegression(max_iter=200))
    ])

    scores = cross_val_score(pipe, X, y, cv=5, scoring="accuracy")

    # Plot
    plt.figure(figsize=(10, 6))
    bars = plt.bar(range(1, 6), scores, color='skyblue', edgecolor='navy', alpha=0.7)
    
    # Add value labels on top of bars
    for i, bar in enumerate(bars):
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height + 0.01,
                f'{height:.3f}', ha='center', va='bottom', fontweight='bold')
    
    plt.xlabel("Fold")
    plt.ylabel("Accuracy")
    plt.title("Pipeline with Scaling + Logistic Regression")
    plt.ylim(0, 1.1)
    plt.grid(True, alpha=0.3, axis='y')
    plt.xticks(range(1, 6))
    plt.tight_layout()
    plt.show()

    return scores.mean()