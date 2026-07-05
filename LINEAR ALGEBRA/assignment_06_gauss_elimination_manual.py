# -------------------------------------------------------------
# Assignment 6
#
# Question 6
# Use Gauss Elimination to solve the following equations
# and verify the solution with NumPy's built-in solver.
#
# 4x1 + 3x2 - 5x3 = 2
# -2x1 - 4x2 + 5x3 = 5
# 8x1 + 8x2 + 0x3 = -3
#
# Hint:
# Manually implement row reduction logic and verify
# the result using np.linalg.solve()
# -------------------------------------------------------------

import numpy as np

# -------------------------------------------------------------
# Coefficient Matrix
# -------------------------------------------------------------
A = np.array([
    [4.0, 3.0, -5.0],
    [-2.0, -4.0, 5.0],
    [8.0, 8.0, 0.0]
])

# -------------------------------------------------------------
# Constant Matrix
# -------------------------------------------------------------
B = np.array([2.0, 5.0, -3.0])

# -------------------------------------------------------------
# Create Augmented Matrix
# -------------------------------------------------------------
aug = np.column_stack((A, B))

print("Original Augmented Matrix:\n")
print(aug)

n = len(A)

# -------------------------------------------------------------
# Forward Elimination
# -------------------------------------------------------------
for i in range(n):

    # Make pivot element 1
    pivot = aug[i][i]

    for j in range(i, n + 1):
        aug[i][j] = aug[i][j] / pivot

    # Make elements below pivot zero
    for k in range(i + 1, n):

        factor = aug[k][i]

        for j in range(i, n + 1):
            aug[k][j] = aug[k][j] - factor * aug[i][j]

print("\nUpper Triangular Matrix:\n")
print(aug)

# -------------------------------------------------------------
# Back Substitution
# -------------------------------------------------------------
x = np.zeros(n)

for i in range(n - 1, -1, -1):

    x[i] = aug[i][n]

    for j in range(i + 1, n):
        x[i] = x[i] - aug[i][j] * x[j]

print("\nSolution using Gaussian Elimination")

print("x1 =", x[0])
print("x2 =", x[1])
print("x3 =", x[2])

# -------------------------------------------------------------
# Verification using NumPy
# -------------------------------------------------------------
print("\nVerification using np.linalg.solve()")

solution = np.linalg.solve(A, B)

print("x1 =", solution[0])
print("x2 =", solution[1])
print("x3 =", solution[2])