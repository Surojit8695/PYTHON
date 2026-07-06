# Question 21
# A company claims that the average lifetime of its
# LED bulbs is 5000 hours.
#
# Sample Mean = 4850
# Population Standard Deviation = 300
# Sample Size = 40
# Significance Level = 0.05
#
# Perform a One-Sample Z-Test.
#
# Hint:
# Use scipy.stats.norm.cdf()
# -------------------------------------------------------------

import math

from scipy.stats import norm

# -------------------------------------------------------------
# Given Data
# -------------------------------------------------------------
sample_mean = 4850

population_mean = 5000

population_std = 300

sample_size = 40

alpha = 0.05

# -------------------------------------------------------------
# Null and Alternative Hypotheses
# -------------------------------------------------------------
print("Null Hypothesis (H0):")

print("The average lifetime of LED bulbs is 5000 hours.")

print("\nAlternative Hypothesis (H1):")

print("The average lifetime is less than 5000 hours.")

# -------------------------------------------------------------
# Calculate Z-score
# -------------------------------------------------------------
z = (sample_mean - population_mean) / (population_std / math.sqrt(sample_size))

print("\nZ-Statistic =", z)

# -------------------------------------------------------------
# Calculate p-value
# -------------------------------------------------------------
p = norm.cdf(z)

print("P-Value =", p)

# -------------------------------------------------------------
# Decision
# -------------------------------------------------------------
if p < alpha:

    print("\nDecision:")

    print("Reject the Null Hypothesis.")

    print("\nConclusion:")

    print("There is sufficient evidence that the average lifetime is less than 5000 hours.")

else:

    print("\nDecision:")

    print("Fail to Reject the Null Hypothesis.")

    print("\nConclusion:")

    print("There is not enough evidence to conclude that the average lifetime is less than 5000 hours.")