from surprise import Dataset, Reader, SVD
from surprise.model_selection import train_test_split
from surprise import accuracy

# Load built-in dataset (MovieLens 100k)
data = Dataset.load_builtin('ml-100k')

# Split into training and testing sets
trainset, testset = train_test_split(data, test_size=0.25)

# Initialize SVD algorithm
model = SVD()

# Train the model
model.fit(trainset)

# Make predictions
predictions = model.test(testset)

# Evaluate model accuracy
rmse = accuracy.rmse(predictions)
print(f"RMSE (Root Mean Squared Error): {rmse:.4f}")

# Show a sample prediction
sample_pred = predictions[0]
print(f"\nSample prediction:\nUser {sample_pred.uid} likely rated item {sample_pred.iid} as {sample_pred.est:.2f}")