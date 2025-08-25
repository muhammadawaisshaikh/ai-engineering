import matplotlib.pyplot as plt
import seaborn as sns

class ExploratoryAnalysis:
    def __init__(self, data):
        self.data = data

    def price_distribution(self):
        """Show histogram of prices"""
        plt.figure(figsize=(8,5))
        sns.histplot(self.data['prices_(£)'], bins=30, kde=True)
        plt.title("Price Distribution")
        plt.show()

    def store_comparison(self):
        """Compare average prices by store"""
        plt.figure(figsize=(10,6))
        sns.boxplot(x="store", y="prices_(£)", data=self.data)
        plt.title("Store-wise Price Comparison")
        plt.xticks(rotation=45)
        plt.show()