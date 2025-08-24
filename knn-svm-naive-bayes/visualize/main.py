from models import knn_demo, svm_demo, naive_bayes_demo

if __name__ == "__main__":
    print("Visualizing KNN Decision Boundary...")
    knn_demo()

    print("Visualizing SVM Decision Boundary...")
    svm_demo()

    print("Visualizing Naive Bayes Decision Boundary...")
    naive_bayes_demo()