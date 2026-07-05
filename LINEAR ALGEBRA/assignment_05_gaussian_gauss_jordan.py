# -------------------------------------------------------------
# Assignment 5
#
# Question 5
# Solve the following system of linear equations using
# Gaussian Elimination and Gauss–Jordan Method.
# Determine whether the system is consistent or inconsistent.
#
# x + y + z = 6
# 2x + 3y + z = 10
# x + 2y + 2z = 9
#
# Hint:
# Use sympy.Matrix() and rref().
# -------------------------------------------------------------

from sympy import Matrix

# -----------------------------
# Coefficient Matrix
# -----------------------------
A = Matrix([
    [1, 1, 1],
    [2, 3, 1],
    [1, 2, 2]
])

# -----------------------------
# Constant Matrix
# -----------------------------
B = Matrix([
    [6],
    [10],
    [9]
])

# -----------------------------
# Create Augmented Matrix
# -----------------------------
augmented = A.row_join(B)

print("Augmented Matrix:\n")
print(augmented)

# -----------------------------
# Gaussian Elimination
# -----------------------------
print("\nGaussian Elimination (Row Echelon Form):")

gaussian = augmented.echelon_form()

print(gaussian)

# -----------------------------
# Gauss-Jordan Method
# -----------------------------
print("\nGauss-Jordan Method (Reduced Row Echelon Form):")

rref_matrix, pivot = augmented.rref()

print(rref_matrix)

# -----------------------------
# Consistency Check
# -----------------------------
rank_A = A.rank()

rank_aug = augmented.rank()

print("\nRank of Coefficient Matrix =", rank_A)

print("Rank of Augmented Matrix =", rank_aug)

if rank_A == rank_aug:

    print("\nSystem is CONSISTENT.")

    if rank_A == A.cols:

        print("Unique Solution Exists.")

        print("\nSolution:")

        print("x =", rref_matrix[0,3])

        print("y =", rref_matrix[1,3])

        print("z =", rref_matrix[2,3])

    else:

        print("Infinite Solutions.")

else:

    print("\nSystem is INCONSISTENT.")