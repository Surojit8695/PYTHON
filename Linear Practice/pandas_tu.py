import pandas as pd
file="C:\\Users\\suroj\\OneDrive\\Desktop\\PYTHON\\Linear Practice\\seeds.csv"
df=pd.read_csv(file)#read file from a csv file using panda
print(df)
print(df.dtypes)

print("Mean ares:")
print(df.mean(numeric_only=True))

print("Median ares:")
print(df.median(numeric_only=True))

print("Standard division is:")
print(df.std(numeric_only=True))

print("Variance is")
print(df.var(numeric_only=True))
print()
print()
print(df.describe())

