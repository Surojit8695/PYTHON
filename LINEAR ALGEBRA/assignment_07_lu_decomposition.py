# Question 7
# Solve the following system of linear equations using
# LU Decomposition Method. Also verify the solution.
#
# 2x + 3y + z = 1
# 4x + 7y + z = 2
# 6x +18y + z = 3
#
# Hint:
# Use scipy.linalg.lu() to factorize the matrix.
# -------------------------------------------------------------

import numpy as np
from scipy.linalg import lu

# -------------------------------------------------------------
# Coefficient Matrix
# -------------------------------------------------------------
A = np.array([
    [2, 3, 1],
    [4, 7, 1],
    [6,18, 1]
], dtype=float)

# -------------------------------------------------------------
# Constant Matrix
# -------------------------------------------------------------
B = np.array([1, 2, 3], dtype=float)

# -------------------------------------------------------------
# LU Decomposition
# -------------------------------------------------------------
P, L, U = lu(A)

print("Permutation Matrix (P):\n")
print(P)

print("\nLower Triangular Matrix (L):\n")
print(L)

print("\nUpper Triangular Matrix (U):\n")
print(U)

# -------------------------------------------------------------
# Solve the system
# Since PA = LU,
# first solve LY = PB
# then solve UX = Y
# -------------------------------------------------------------
PB = np.dot(P, B)

Y = np.linalg.solve(L, PB)

X = np.linalg.solve(U, Y)

print("\nSolution using LU Decomposition")

print("x =", X[0])

print("y =", X[1])

print("z =", X[2])

# -------------------------------------------------------------
# Verification using NumPy(This part is not mandatory)
# -------------------------------------------------------------
print("\nVerification using np.linalg.solve()")

solution = np.linalg.solve(A, B)

print("x =", solution[0])

print("y =", solution[1])

print("z =", solution[2])