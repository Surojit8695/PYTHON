# -------------------------------------------------------------
# Assignment 18
#
# Question 18
# A researcher wants to test whether there is an
# association between Gender and Product Preference.
#
#            Like   Dislike
# Male        30       20
# Female      10       40
#
# Perform a Chi-Square Test of Independence.
#
# Hint:
# Use scipy.stats.chi2_contingency()
# -------------------------------------------------------------

import numpy as np

from scipy.stats import chi2_contingency

# -------------------------------------------------------------
# Contingency Table
# -------------------------------------------------------------
table = np.array([
    [30, 20],
    [10, 40]
])

print("Contingency Table\n")

print(table)

# -------------------------------------------------------------
# Hypotheses
# -------------------------------------------------------------
print("\nNull Hypothesis (H0):")

print("Gender and Product Preference are independent.")

print("\nAlternative Hypothesis (H1):")

print("Gender and Product Preference are associated.")

# -------------------------------------------------------------
# Significance Level
# -------------------------------------------------------------
alpha = 0.05

print("\nSignificance Level =", alpha)

# -------------------------------------------------------------
# Perform Chi-Square Test
# -------------------------------------------------------------
chi2, p, dof, expected = chi2_contingency(table)

print("\nChi-Square Statistic =", chi2)

print("P-Value =", p)

print("Degrees of Freedom =", dof)

print("\nExpected Frequency Table\n")

print(expected)

# -------------------------------------------------------------
# Decision
# -------------------------------------------------------------
if p < alpha:

    print("\nDecision:")

    print("Reject the Null Hypothesis.")

    print("\nConclusion:")

    print("There is a significant association between Gender and Product Preference.")

else:

    print("\nDecision:")

    print("Fail to Reject the Null Hypothesis.")

    print("\nConclusion:")

    print("Gender and Product Preference are independent.")