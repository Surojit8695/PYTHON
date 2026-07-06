# Question 13
# Using the Pima Indians Diabetes dataset,
# compute the first four moments and compare
# them using histograms, boxplots and bar charts.
#
# Hint:
# Use mean(), var(), skew(), kurtosis(),
# plt.hist(), plt.boxplot().
# -------------------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------------------------------------
# Create Sample Diabetes Dataset
# -------------------------------------------------------------
# data = {
#     "Glucose": [85, 89, 120, 140, 155, 170, 110, 95],
#     "BloodPressure": [66, 70, 72, 80, 85, 90, 75, 68],
#     "SkinThickness": [22, 24, 30, 32, 35, 38, 28, 25],
#     "Insulin": [90, 100, 120, 140, 180, 210, 130, 110],
#     "BMI": [22.5, 24.0, 27.5, 30.2, 33.8, 36.1, 28.4, 25.6]
# }

# df = pd.DataFrame(data)
file1="C:\\Users\\suroj\\OneDrive\\Desktop\\PYTHON\\LINEAR ALGEBRA\\sample_diabetes_dataset.csv"
df = pd.read_csv(file1)

# -------------------------------------------------------------
# Display Dataset
# -------------------------------------------------------------
print("Sample Diabetes Dataset\n")
print(df)

# -------------------------------------------------------------
# Display Data Types
# -------------------------------------------------------------
print("\nData Types\n")
print(df.dtypes)

# -------------------------------------------------------------
# First Four Moments
# -------------------------------------------------------------
print("\nMean\n")
print(df.mean())

print("\nVariance\n")
print(df.var())

print("\nSkewness\n")
print(df.skew())

print("\nKurtosis\n")
print(df.kurt())

# -------------------------------------------------------------
# Histograms
# -------------------------------------------------------------
plt.figure(figsize=(10,8))
df.hist()
plt.suptitle("Histograms")
plt.show()

# Boxplots
# -------------------------------------------------------------
plt.figure(figsize=(8,6))
df.boxplot()
plt.title("Boxplots")
plt.show()

# Bar Chart - Mean
df.mean().plot(kind="bar")
plt.title("Mean of Variables")
plt.ylabel("Mean")
plt.show()

# -------------------------------------------------------------
# Bar Chart - Variance
# -------------------------------------------------------------
df.var().plot(kind="bar")
plt.title("Variance of Variables")
plt.ylabel("Variance")
plt.show()

# -------------------------------------------------------------
# Bar Chart - Skewness
# -------------------------------------------------------------
df.skew().plot(kind="bar")
plt.title("Skewness of Variables")
plt.ylabel("Skewness")
plt.show()

# -------------------------------------------------------------
# Bar Chart - Kurtosis
# -------------------------------------------------------------
df.kurt().plot(kind="bar")
plt.title("Kurtosis of Variables")
plt.ylabel("Kurtosis")
plt.show()