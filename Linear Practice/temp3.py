# Question 12
# Using the Seeds dataset, identify the data type of each
# variable and compute appropriate measures of central
# tendency and dispersion for the numerical variables.
#
# Hint:
# Use pandas functions like df.describe(),
# mean(), median(), std().
# -------------------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt

#if we dont create csv we can create data like this
# data = {
#     "Area": [15.2, 14.8, 16.1, 15.7, 16.3],
#     "Perimeter": [14.1, 13.8, 14.5, 14.3, 14.7],
#     "Compactness": [0.87, 0.85, 0.89, 0.88, 0.90],
#     "Kernel_Length": [5.6, 5.4, 5.9, 5.8, 6.0],
#     "Kernel_Width": [3.3, 3.2, 3.4, 3.3, 3.5],
#     "Class": ["Kama", "Rosa", "Canadian", "Kama", "Rosa"]
# }
#this is how we can read the csv file using pandas
# df = pd.DataFrame(data)# convert the data into csv file
file1="C:\\Users\\suroj\\OneDrive\\Desktop\\PYTHON\\LINEAR ALGEBRA\\seeds.csv"
df = pd.read_csv(file1)
#display dataset
print("Seeds Dataset\n")
print(df)

# Data Types
print("\nData Types\n")
print(df.dtypes)

# Mean
print("\nMean\n")
print(df.mean(numeric_only=True))


# Median
print("\nMedian\n")
print(df.median(numeric_only=True))

# Variance
print("\nVariance\n")
print(df.var(numeric_only=True))

# -------------------------------------------------------------
# Standard Deviation
# -------------------------------------------------------------
print("\nStandard Deviation\n")

print(df.std(numeric_only=True))

# -------------------------------------------------------------
# Summary Statistics
# -------------------------------------------------------------
print("\nSummary Statistics\n")

print(df.describe())

df.hist()
plt.show()

df.boxplot()
plt.show()

df.mean(numeric_only=True).plot(kind="bar")
plt.show()