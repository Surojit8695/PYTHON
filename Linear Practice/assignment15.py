import pandas as pd
import matplotlib.pyplot as plt
file1="C:\\Users\\suroj\\OneDrive\\Desktop\\PYTHON\\LINEAR ALGEBRA\\glass_sample.csv"
df=pd.read_csv(file1)
print(df)

print(df.dtypes)

print(df.select_dtypes(include="number").columns)

freq_ri=pd.cut(df["RI"],bins=10).value_counts().sort_index()
print(freq_ri)

freq_Na=pd.cut(df["Na"],bins=10).value_counts().sort_index()
print(freq_Na)

freq_Mg=pd.cut(df["Mg"],bins=10).value_counts().sort_index()
print(freq_Mg)


df.hist(figsize=(8,4))
plt.show()







