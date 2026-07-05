# -------------------------------------------------------------
# Assignment 22
#
# Question 22
# A nutritionist claims that a new diet plan reduces
# average cholesterol levels to below 200 mg/dL.
#
# Sample Mean = 192 mg/dL
# Sample Standard Deviation = 15 mg/dL
# Sample Size = 25
# Significance Level = 0.05
#
# Perform a One-Sample t-Test.
#
# Hint:
# Use scipy.stats.t.cdf()
# -------------------------------------------------------------

import math

from scipy.stats import t

# -------------------------------------------------------------
# Given Data
# -------------------------------------------------------------
sample_mean = 192

population_mean = 200

sample_std = 15

sample_size = 25

alpha = 0.05

# -------------------------------------------------------------
# Null and Alternative Hypotheses
# -------------------------------------------------------------
print("Null Hypothesis (H0):")

print("The average cholesterol level is 200 mg/dL.")

print("\nAlternative Hypothesis (H1):")

print("The average cholesterol level is less than 200 mg/dL.")

# -------------------------------------------------------------
# Degrees of Freedom
# -------------------------------------------------------------
df = sample_size - 1

# -------------------------------------------------------------
# Calculate t-statistic
# -------------------------------------------------------------
t_stat = (sample_mean - population_mean) / (sample_std / math.sqrt(sample_size))

print("\nt-Statistic =", t_stat)

# -------------------------------------------------------------
# Calculate p-value
# -------------------------------------------------------------
p_value = t.cdf(t_stat, df)

print("P-Value =", p_value)

# -------------------------------------------------------------
# Decision
# -------------------------------------------------------------
if p_value < alpha:

    print("\nDecision:")

    print("Reject the Null Hypothesis.")

    print("\nConclusion:")

    print("There is sufficient evidence that the average cholesterol level is below 200 mg/dL.")

else:

    print("\nDecision:")

    print("Fail to Reject the Null Hypothesis.")

    print("\nConclusion:")

    print("There is not enough evidence to conclude that the average cholesterol level is below 200 mg/dL.")