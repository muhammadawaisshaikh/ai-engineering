from sklearn.model_selection import train_test_split
from imbalance_analysis import load_imbalanced_data, analyze_distribution
from resampling_methods import oversample_data, undersample_data
from smote_handler import apply_smote
from weighted_model import train_weighted_model
from evaluation import evaluate_model
from sklearn.linear_model import LogisticRegression

# Step 1: Load imbalanced data
X, y = load_imbalanced_data()
analyze_distribution(y)

# Step 2: Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Step 3: Apply SMOTE (can try oversample/undersample too)
X_res, y_res = apply_smote(X_train, y_train)

# Step 4: Train baseline model
baseline_model = LogisticRegression(random_state=42)
baseline_model.fit(X_train, y_train)
baseline_preds = baseline_model.predict(X_test)
baseline_probs = baseline_model.predict_proba(X_test)[:,1]
print("\n=== Baseline Model (No Balancing) ===")
evaluate_model(y_test, baseline_preds, baseline_probs)

# Step 5: Train weighted model
print("\n=== Weighted Model (Class Weights) ===")
train_weighted_model(X_res, y_res, X_test, y_test)
