# Question 23 (Not Done)
# A researcher wants to compare the average weights
# of two different plant species.
#
# Species A:
# 12.5, 13.1, 11.8, 12.9, 13.3
#
# Species B:
# 14.2, 13.8, 14.5, 14.0, 13.9
#
# Perform an Independent Two-Sample t-Test
# at the 5% significance level.
#
# Hint:
# Use scipy.stats.ttest_ind()
# -------------------------------------------------------------

from scipy.stats import ttest_ind

# -------------------------------------------------------------
# Sample Data
# -------------------------------------------------------------
species_A = [12.5, 13.1, 11.8, 12.9, 13.3]

species_B = [14.2, 13.8, 14.5, 14.0, 13.9]

# -------------------------------------------------------------
# Null and Alternative Hypotheses
# -------------------------------------------------------------
print("Null Hypothesis (H0):")
print("The mean weights of Species A and Species B are equal.")

print("\nAlternative Hypothesis (H1):")
print("The mean weights of Species A and Species B are different.")

# -------------------------------------------------------------
# Significance Level
# -------------------------------------------------------------
alpha = 0.05

print("\nSignificance Level =", alpha)

# -------------------------------------------------------------
# Perform Independent Two-Sample t-Test
# -------------------------------------------------------------
t_stat, p_value = ttest_ind(species_A, species_B)

print("\nt-Statistic =", t_stat)

print("P-Value =", p_value)

# -------------------------------------------------------------
# Decision
# -------------------------------------------------------------
if p_value < alpha:

    print("\nDecision:")
    print("Reject the Null Hypothesis.")

    print("\nConclusion:")
    print("There is a significant difference in the mean weights of the two species.")

else:

    print("\nDecision:")
    print("Fail to Reject the Null Hypothesis.")

    print("\nConclusion:")
    print("There is no significant difference in the mean weights of the two species.")