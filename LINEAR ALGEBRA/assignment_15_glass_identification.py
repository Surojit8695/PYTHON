# Question 15(Same as 14)
# Using the Glass Identification dataset,
# identify the numerical variables and construct
# frequency distributions for RI, Na and Mg.
#
# Plot histograms for these variables.
#
# Hint:
# Use df.select_dtypes(), pd.cut(),
# value_counts() and plt.hist().
# -------------------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------------------------------------
# Create Sample Glass Dataset
# -------------------------------------------------------------
data = {
    "RI": [1.517, 1.518, 1.519, 1.520, 1.521,
           1.522, 1.518, 1.519, 1.520, 1.521],

    "Na": [13.2, 13.5, 13.8, 14.0, 14.2,
           14.5, 13.7, 13.9, 14.1, 14.4],

    "Mg": [3.50, 3.45, 3.60, 3.55, 3.40,
           3.35, 3.50, 3.48, 3.52, 3.46]
}

df = pd.DataFrame(data)

# -------------------------------------------------------------
# Display Dataset
# -------------------------------------------------------------
print("Sample Glass Dataset\n")

print(df)

# -------------------------------------------------------------
# Display Data Types
# -------------------------------------------------------------
print("\nData Types\n")

print(df.dtypes)

# -------------------------------------------------------------
# Identify Numerical Variables
# -------------------------------------------------------------
print("\nNumerical Variables\n")

print(df.select_dtypes(include="number").columns)

# -------------------------------------------------------------
# Frequency Distribution : RI
# -------------------------------------------------------------
print("\nFrequency Distribution of RI\n")

ri_freq = pd.cut(df["RI"], bins=5).value_counts().sort_index()

print(ri_freq)

# -------------------------------------------------------------
# Frequency Distribution : Sodium
# -------------------------------------------------------------
print("\nFrequency Distribution of Na\n")

na_freq = pd.cut(df["Na"], bins=5).value_counts().sort_index()

print(na_freq)

# -------------------------------------------------------------
# Frequency Distribution : Magnesium
# -------------------------------------------------------------
print("\nFrequency Distribution of Mg\n")

mg_freq = pd.cut(df["Mg"], bins=5).value_counts().sort_index()

print(mg_freq)

# -------------------------------------------------------------
# Histogram : RI
# -------------------------------------------------------------
plt.figure(figsize=(6,4))

plt.hist(df["RI"], bins=5)

plt.title("Histogram of Refractive Index (RI)")

plt.xlabel("RI")

plt.ylabel("Frequency")

plt.show()

# -------------------------------------------------------------
# Histogram : Sodium
# -------------------------------------------------------------
plt.figure(figsize=(6,4))

plt.hist(df["Na"], bins=5)

plt.title("Histogram of Sodium (Na)")

plt.xlabel("Na")

plt.ylabel("Frequency")

plt.show()

# -------------------------------------------------------------
# Histogram : Magnesium
# -------------------------------------------------------------
plt.figure(figsize=(6,4))

plt.hist(df["Mg"], bins=5)

plt.title("Histogram of Magnesium (Mg)")

plt.xlabel("Mg")

plt.ylabel("Frequency")

plt.show()