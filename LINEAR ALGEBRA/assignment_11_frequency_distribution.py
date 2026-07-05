# Question 11
# Draw suitable diagrams to represent both absolute and
# cumulative frequencies for the given family size data.
#
# Hint:
# Use plt.bar() for absolute frequency and
# plt.plot(np.cumsum(frequency)) for cumulative frequency.
# -------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt

# -------------------------------------------------------------
# Given Data
# -------------------------------------------------------------
family_size = [2, 3, 4, 5, 6, 7, 8, 9, 10]

frequency = [26, 21, 17, 12, 9, 3, 2, 2, 1]

# -------------------------------------------------------------
# Absolute Frequency (Bar Chart)
# -------------------------------------------------------------
plt.figure(figsize=(8,5))

plt.bar(family_size, frequency)

plt.title("Absolute Frequency Distribution")

plt.xlabel("Family Size")

plt.ylabel("Frequency")

plt.grid(axis='y')

plt.show()

# -------------------------------------------------------------
# Cumulative Frequency
# -------------------------------------------------------------
cumulative_frequency = np.cumsum(frequency)

print("Cumulative Frequency:")

print(cumulative_frequency)

# -------------------------------------------------------------
# Cumulative Frequency Graph (Ogive)
# -------------------------------------------------------------
plt.figure(figsize=(8,5))

plt.plot(family_size,
         cumulative_frequency,
         marker='o')

plt.title("Cumulative Frequency Distribution")

plt.xlabel("Family Size")

plt.ylabel("Cumulative Frequency")

plt.grid(True)

plt.show()