# Question 5
# Solve the following system of linear equations using
# Gaussian Elimination and determine whether the system
# is consistent or inconsistent.
#
# x + y + z = 6
# 2x + 3y + z = 10
# x + 2y + 2z = 9
#
# Hint:
# Use sympy.Matrix() and echelon_form().
# -------------------------------------------------------------

from sympy import Matrix

# -------------------------------------------------------------
# Coefficient Matrix
# -------------------------------------------------------------
A = [
    [1, 1, 1],
    [2, 3, 1],
    [1, 2, 2]
]
A=Matrix(A)#SymPy Matrix objects.

# -------------------------------------------------------------
# Constant Matrix
# -------------------------------------------------------------
B = [
    [6],
    [10],
    [9]
]
B=Matrix(B)#SymPy Matrix objects.

# -------------------------------------------------------------
# Create Augmented Matrix
# -------------------------------------------------------------
augmented = A.row_join(B)

print("Original Augmented Matrix:\n")
print(augmented)

# -------------------------------------------------------------
# Gaussian Elimination
# Convert to Row Echelon Form (Upper Triangular Matrix)
# -------------------------------------------------------------
print("\nRow Echelon Form:\n")

REF = augmented.echelon_form()

print(REF)

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
        #back substution
        z = REF[2,3] / REF[2,2]

        y = (REF[1,3] - REF[1,2] * z) / REF[1,1]

        x = (REF[0,3] - REF[0,1] * y - REF[0,2] * z) / REF[0,0]

        print("\nSolution using Back Substitution")
        print("x =", x)
        print("y =", y)
        print("z =", z)
    else:
        print("Infinite Solutions.")
else:
    print("\nSystem is INCONSISTENT.")