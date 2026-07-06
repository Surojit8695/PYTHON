# Question 17
# A teacher wants to know if three different teaching
# methods produce different average exam scores.
#
# Method A : 78, 85, 82, 88
# Method B : 72, 75, 68, 70
# Method C : 90, 95, 92, 88
#
# Perform a One-Way ANOVA test at the 5%
# significance level.
#
# Hint:
# Use scipy.stats.f_oneway()
# -------------------------------------------------------------
from scipy.stats import f_oneway

# -------------------------------------------------------------
# Exam Scores
# -------------------------------------------------------------
method_A = [78, 85, 82, 88]

method_B = [72, 75, 68, 70]

method_C = [90, 95, 92, 88]

# Hypotheses
print("Null Hypothesis (H0):")

print("The mean scores of all teaching methods are equal.")

print("\nAlternative Hypothesis (H1):")

print("At least one teaching method has a different mean score.")

# -------------------------------------------------------------
# Significance Level
# -------------------------------------------------------------
alpha = 0.05
# print(5/100)

print("\nSignificance Level =", alpha)

# -------------------------------------------------------------
# Perform One-Way ANOVA
# -------------------------------------------------------------
F, p = f_oneway(method_A,
                method_B,
                method_C)

print("\nF-Statistic =", F)

print("P-Value =", p)

# -------------------------------------------------------------
# Construct Simple ANOVA Table
# -------------------------------------------------------------
k = 3                      # Number of groups

N = len(method_A) + len(method_B) + len(method_C)

print("\nANOVA TABLE")

print("----------------------------------------------")

print("Source\t\tDF")

print("Between Groups\t", k - 1)

print("Within Groups\t", N - k)

print("Total\t\t", N - 1)

print("----------------------------------------------")

# -------------------------------------------------------------
# Decision
# -------------------------------------------------------------
if p < alpha:

    print("\nDecision:")

    print("Reject the Null Hypothesis.")

    print("\nConclusion:")

    print("The teaching methods produce significantly different mean scores.")

else:

    print("\nDecision:")

    print("Fail to Reject the Null Hypothesis.")

    print("\nConclusion:")

    print("There is no significant difference in the mean scores.")