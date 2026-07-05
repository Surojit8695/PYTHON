# -------------------------------------------------------------
# Assignment 24
#
# Question 24
# A fair coin is tossed 10 times.
#
# Model the number of heads as a Binomial
# random variable.
#
# Compute:
# 1. Probability of getting exactly 6 heads.
# 2. Probability of getting at most 3 heads.
#
# Plot the Probability Mass Function (PMF).
#
# Hint:
# Use scipy.stats.binom
# -------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt

from scipy.stats import binom

# -------------------------------------------------------------
# Number of Trials
# -------------------------------------------------------------
n = 10

# -------------------------------------------------------------
# Probability of Head
# -------------------------------------------------------------
p = 0.5

# -------------------------------------------------------------
# Probability of Exactly 6 Heads
# -------------------------------------------------------------
exactly_6 = binom.pmf(6, n, p)

print("Probability of Exactly 6 Heads =")

print(exactly_6)

# -------------------------------------------------------------
# Probability of At Most 3 Heads
# -------------------------------------------------------------
at_most_3 = binom.cdf(3, n, p)

print("\nProbability of At Most 3 Heads =")

print(at_most_3)

# -------------------------------------------------------------
# Probability Mass Function
# -------------------------------------------------------------
x = np.arange(0, n + 1)

pmf = binom.pmf(x, n, p)

# -------------------------------------------------------------
# Plot PMF
# -------------------------------------------------------------
plt.figure(figsize=(8,5))

plt.bar(x, pmf)

plt.title("Binomial Distribution (n = 10, p = 0.5)")

plt.xlabel("Number of Heads")

plt.ylabel("Probability")

plt.grid(axis="y")

plt.show()