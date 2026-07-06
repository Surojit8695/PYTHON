# Question 19 (Not Done)
# Using the Iris dataset, compute skewness
# and kurtosis for Sepal Length and interpret
# the distribution shape.
#
# Hint:
# Use scipy.stats.skew()
# and scipy.stats.kurtosis()
# -------------------------------------------------------------

from sklearn.datasets import load_iris

from scipy.stats import skew, kurtosis

# -------------------------------------------------------------
# Load Iris Dataset
# -------------------------------------------------------------
iris = load_iris()

# -------------------------------------------------------------
# Extract Sepal Length (Column 0)
# -------------------------------------------------------------
sepal_length = iris.data[:, 0]

# -------------------------------------------------------------
# Compute Skewness
# -------------------------------------------------------------
skewness = skew(sepal_length)

# -------------------------------------------------------------
# Compute Kurtosis
# -------------------------------------------------------------
kurt = kurtosis(sepal_length)

# -------------------------------------------------------------
# Display Results
# -------------------------------------------------------------
print("Skewness =", skewness)

print("Kurtosis =", kurt)

# -------------------------------------------------------------
# Interpretation of Skewness
# -------------------------------------------------------------
if skewness > 0:

    print("\nDistribution is Positively (Right) Skewed.")

elif skewness < 0:

    print("\nDistribution is Negatively (Left) Skewed.")

else:

    print("\nDistribution is Symmetric.")

# -------------------------------------------------------------
# Interpretation of Kurtosis
# -------------------------------------------------------------
if kurt > 0:

    print("Distribution is Leptokurtic (More Peaked).")

elif kurt < 0:

    print("Distribution is Platykurtic (Flatter).")

else:

    print("Distribution is Mesokurtic (Normal).")