from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Example data: [Annual Income, Spending Score]
data = [[15, 39], [16, 81], [17, 6], [18, 77], [19, 40], [20, 76], [21, 6], [22, 77]]

kmeans = KMeans(n_clusters=2)
kmeans.fit(data)

# Plotting
plt.scatter(*zip(*data), c=kmeans.labels_)
plt.title("Customer Segmentation")
plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.show()