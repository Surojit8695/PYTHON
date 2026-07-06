# Question 9(PCA)  (Not Done)
# Standardize the features and reduce the
# dimensionality to two principal components.
#
# Plot the transformed data using different
# colors for different species.
#
# Hint:
# Use StandardScaler and PCA(n_components=2)
# -------------------------------------------------------------

import matplotlib.pyplot as plt

from sklearn.datasets import load_iris

from sklearn.preprocessing import StandardScaler

from sklearn.decomposition import PCA

# -------------------------------------------------------------
# Load Iris Dataset
# -------------------------------------------------------------
iris = load_iris()

# Feature Matrix
X = iris.data

# Target (Species)
y = iris.target

# Species Names
target_names = iris.target_names

# -------------------------------------------------------------
# Standardize the Features
# -------------------------------------------------------------
scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

# -------------------------------------------------------------
# Apply PCA
# -------------------------------------------------------------
pca = PCA(n_components=2)

X_pca = pca.fit_transform(X_scaled)

# -------------------------------------------------------------
# Display Explained Variance
# -------------------------------------------------------------
print("Explained Variance Ratio:")

print(pca.explained_variance_ratio_)

# -------------------------------------------------------------
# Plot PCA Graph
# -------------------------------------------------------------
plt.figure(figsize=(8,6))

colors = ['red', 'green', 'blue']

for i in range(3):

    plt.scatter(
        X_pca[y == i, 0],
        X_pca[y == i, 1],
        color=colors[i],
        label=target_names[i]
    )

plt.title("PCA of Iris Dataset")

plt.xlabel("Principal Component 1")

plt.ylabel("Principal Component 2")

plt.legend()

plt.grid(True)

plt.show()