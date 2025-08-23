from utils.data_loader import load_classification_data
from models.tree_forest import train_decision_tree, train_random_forest

if __name__ == "__main__":
    # Decision Tree & Random Forest
    X_train, X_test, y_train, y_test = load_classification_data()

    tree_acc = train_decision_tree(X_train, X_test, y_train, y_test)
    forest_acc = train_random_forest(X_train, X_test, y_train, y_test)

    print(f"Decision Tree Accuracy: {tree_acc:.2f}")
    print(f"Random Forest Accuracy: {forest_acc:.2f}")