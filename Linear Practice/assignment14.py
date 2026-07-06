import pandas as pd
import matplotlib.pyplot as plt
file1="C:\\Users\\suroj\\OneDrive\\Desktop\\PYTHON\\LINEAR ALGEBRA\\breast_cancer_sample.csv"
df=pd.read_csv(file1)
print(df)

print(df.select_dtypes(include="number"))

print()
f1=pd.cut(df["Mean_Radius"],bins=10).value_counts().sort_index()
print(f1)

print()
f2=pd.cut(df["Mean_Texture"],bins=10).value_counts().sort_index()
print(f2)

print()
f3=pd.cut(df["Mean_Perimeter"],bins=10).value_counts().sort_index()
print(f3)

feature=["Mean_Radius","Mean_Texture","Mean_Perimeter"]
#histogram
df.hist()
plt.show()






