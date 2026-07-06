# Question 14
# Using the Breast Cancer dataset, identify the
# numerical variables and construct frequency
# distributions for Mean Radius, Mean Texture,
# and Mean Perimeter.
#
# Plot histograms for these variables.
#
# Hint:
# Use pd.cut(), value_counts() and plt.hist().
# -------------------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------------------------------------
# Create Sample Breast Cancer Dataset
# -------------------------------------------------------------
data = {
    "Mean_Radius": [11.5, 12.3, 13.8, 14.5, 15.2, 16.4, 17.1, 18.6, 19.4, 20.1],
    "Mean_Texture": [15.2, 16.5, 18.1, 19.0, 20.5, 21.2, 22.6, 23.5, 24.8, 25.4],
    "Mean_Perimeter": [75, 80, 85, 90, 95, 100, 105, 110, 115, 120]
}

df = pd.DataFrame(data)

# -------------------------------------------------------------
# Display Dataset
# -------------------------------------------------------------
print("Sample Breast Cancer Dataset\n")

print(df)

# -------------------------------------------------------------
# Display Data Types
# -------------------------------------------------------------
print("\nData Types\n")

print(df.dtypes)