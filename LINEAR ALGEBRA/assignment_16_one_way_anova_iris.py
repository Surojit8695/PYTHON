# Question 16(Dificult)
# Using the Iris dataset, perform a One-Way ANOVA
# to test whether there is a significant difference
# in sepal length across the three species.
#
# State the null hypothesis, alternative hypothesis,
# significance level and interpret the result.
#
# Hint:
# Use scipy.stats.f_oneway()
# -------------------------------------------------------------

from sklearn.datasets import load_iris
from scipy.stats import f_oneway

# -------------------------------------------------------------
# Load Iris Dataset
# -------------------------------------------------------------
iris = load_iris()

X = iris.data

y = iris.target

species = iris.target_names

# -------------------------------------------------------------
# Sepal Length (Column 0)
# -------------------------------------------------------------
setosa = X[y == 0, 0]

versicolor = X[y == 1, 0]

virginica = X[y == 2, 0]

# -------------------------------------------------------------
# Null and Alternative Hypotheses
# -------------------------------------------------------------
print("Null Hypothesis (H0):")
print("Mean sepal lengths of all species are equal.")

print("\nAlternative Hypothesis (H1):")
print("At least one species has a different mean sepal length.")

# -------------------------------------------------------------
# Significance Level
# -------------------------------------------------------------
alpha = 0.05

print("\nSignificance Level =", alpha)

# -------------------------------------------------------------
# One-Way ANOVA
# -------------------------------------------------------------
F, p = f_oneway(setosa,
                versicolor,
                virginica)

print("\nF-Statistic =", F)

print("P-Value =", p)

# -------------------------------------------------------------
# Decision
# -------------------------------------------------------------
if p < alpha:

    print("\nReject the Null Hypothesis.")

    print("There is a significant difference in sepal length among the three species.")

else:

    print("\nFail to Reject the Null Hypothesis.")

    print("No significant difference found.")

# -------------------------------------------------------------
# Type I and Type II Errors
# -------------------------------------------------------------
print("\nType I Error:")
print("Rejecting H0 when it is actually true.")

print("\nType II Error:")
print("Failing to reject H0 when it is actually false.")