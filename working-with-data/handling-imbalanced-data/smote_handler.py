from imblearn.over_sampling import SMOTE

def apply_smote(X, y):
    """Use SMOTE to generate synthetic samples for the minority class."""
    smote = SMOTE(random_state=42)
    X_res, y_res = smote.fit_resample(X, y)
    return X_res, y_res