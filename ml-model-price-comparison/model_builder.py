from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

class ModelBuilder:
    def __init__(self, data):
        self.data = data
        self.model = LinearRegression()

    def train_model(self):
        X = self.data.drop("prices_(£)", axis=1)
        y = self.data["prices_(£)"]

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        self.model.fit(X_train, y_train)
        return self.model, X_test, y_test