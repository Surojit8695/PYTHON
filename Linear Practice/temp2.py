# Question 13
# Using the Pima Indians Diabetes dataset,
# compute the first four moments and compare
# them using histograms, boxplots and bar charts.
#
# Hint:
# Use mean(), var(), skew(), kurtosis(),
# plt.hist(), plt.boxplot().
import pandas as pd
import matplotlib.pyplot as plt
file1="C:\\Users\\suroj\\OneDrive\\Desktop\\PYTHON\\LINEAR ALGEBRA\\sample_diabetes_dataset.csv"

df=pd.read_csv(file1)
print(df)

print(df.dtypes)

print(df.mean(numeric_only=True))
print(df.median())
print(df.skew())
print(df.kurtosis())

#histogram
df.hist()
plt.suptitle("Histogram")
plt.show()

#boxplot
df.boxplot()
plt.show()

#bar chart for mean
df.mean().plot(kind="bar")
plt.title("Mean of variance")
plt.show()

#bar chart for median
df.median().plot(kind="bar")
plt.show()

#bar chart for variance
df.var().plot(kind="bar")
plt.show()

#bar chart for kurtosis
df.skew().plot(kind="bar")
plt.show()

