# Question 5
# Solve the following system of linear equations using
# Gauss–Jordan Method and determine whether the system
# is consistent or inconsistent.
#
# x + y + z = 6
# 2x + 3y + z = 10
# x + 2y + 2z = 9
#
# Hint:
# Use sympy.Matrix() and rref().
# -------------------------------------------------------------

from sympy import Matrix

# -------------------------------------------------------------
# Coefficient Matrix
# -------------------------------------------------------------
A = Matrix([
    [1, 1, 1],
    [2, 3, 1],
    [1, 2, 2]
])

# -------------------------------------------------------------
# Constant Matrix
# -------------------------------------------------------------
B = Matrix([
    [6],
    [10],
    [9]
])

# -------------------------------------------------------------
# Create Augmented Matrix
# -------------------------------------------------------------
augmented = A.row_join(B)

print("Original Augmented Matrix:\n")
print(augmented)

# -------------------------------------------------------------
# Gauss-Jordan Elimination
# Convert to Reduced Row Echelon Form (RREF)
# -------------------------------------------------------------
print("\nReduced Row Echelon Form (RREF):\n")

RREF, pivot = augmented.rref()

print(RREF)

# -------------------------------------------------------------
# Check Consistency
# -------------------------------------------------------------
rank_A = A.rank()

rank_aug = augmented.rank()

print("\nRank of Coefficient Matrix =", rank_A)

print("Rank of Augmented Matrix =", rank_aug)

if rank_A == rank_aug:

    print("\nSystem is CONSISTENT.")

    if rank_A == A.cols:

        print("Unique Solution Exists.")

        print("\nSolution")

        print("x =", RREF[0,3])

        print("y =", RREF[1,3])

        print("z =", RREF[2,3])

    else:

        print("Infinite Solutions.")

else:

    print("\nSystem is INCONSISTENT.")