import pandas as pd
import matplotlib.pyplot as plt
file1="C:\\Users\\suroj\\OneDrive\\Desktop\\PYTHON\\Linear Practice\\seeds.csv"
df=pd.read_csv(file1)

#print(df)
print(df.dtypes)

print()
print("Mean:\n",df.mean(numeric_only=True))
print()
print("Median:\n",df.median(numeric_only=True))
print()
print("Standard:\n",df.std(numeric_only=True))
print()
print("Variance:\n",df.var(numeric_only=True))

print(df.columns)
# print()
# print("Summary:\n",df.describe())

# #histogram
# df.hist(figsize=(10,6))
# plt.suptitle("Histogram")
# plt.show()

# #boxplot
# df.boxplot(figsize=(10,6))
# plt.suptitle("Boxplot")
# plt.show()

# #bar chart for each column
mean=df.mean(numeric_only=True)
print(mean)

# plt.figure(figsize=(8,4))
# plt.bar(mean.index,mean.values)
# plt.show()

plt.figure(figsize=(8,4))
df.mean(numeric_only=True).plot(kind="bar")
plt.show()

