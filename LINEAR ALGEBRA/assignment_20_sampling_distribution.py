# -------------------------------------------------------------
# Assignment 20
#
# Question 20
# Using the Iris dataset, draw 100 repeated random
# samples of size 30 and compute the sample means
# of sepal length.
#
# Plot the sampling distribution of the sample mean
# and compare it with the original distribution.
#
# Hint:
# Use np.random.choice() and plt.hist().
# -------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris

# -------------------------------------------------------------
# Load Iris Dataset
# -------------------------------------------------------------
iris = load_iris()

# -------------------------------------------------------------
# Extract Sepal Length
# -------------------------------------------------------------
sepal_length = iris.data[:, 0]

# -------------------------------------------------------------
# Draw 100 Samples
# -------------------------------------------------------------
sample_means = []

for i in range(100):

    sample = np.random.choice(sepal_length,
                              size=30,
                              replace=True)

    sample_means.append(np.mean(sample))

sample_means = np.array(sample_means)

# -------------------------------------------------------------
# Mean and Variance
# -------------------------------------------------------------
print("Original Mean =", np.mean(sepal_length))

print("Original Variance =", np.var(sepal_length))

print("\nMean of Sample Means =", np.mean(sample_means))

print("Variance of Sample Means =", np.var(sample_means))

# -------------------------------------------------------------
# Histogram of Original Data
# -------------------------------------------------------------
plt.figure(figsize=(7,5))

plt.hist(sepal_length,
         bins=10)

plt.title("Original Distribution of Sepal Length")

plt.xlabel("Sepal Length")

plt.ylabel("Frequency")

plt.grid(True)

plt.show()

# -------------------------------------------------------------
# Histogram of Sample Means
# -------------------------------------------------------------
plt.figure(figsize=(7,5))

plt.hist(sample_means,
         bins=10)

plt.title("Sampling Distribution of Sample Mean")

plt.xlabel("Sample Mean")

plt.ylabel("Frequency")

plt.grid(True)

plt.show()