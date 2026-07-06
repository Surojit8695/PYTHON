# Question 9
# Consider the vectors
#
# v1 = (1,1,0)
# v2 = (0,1,1)
# v3 = (1,2,1)
#
# Check whether they are linearly independent.
# Find a basis for the subspace they span and
# determine its dimension.
#
# Hint:
# Use sympy.Matrix(), rank() and rref().
# -------------------------------------------------------------

from sympy import Matrix

# -------------------------------------------------------------
# Create Matrix
# (Each column represents a vector)
# -------------------------------------------------------------
A = Matrix([
    [1, 0, 1],
    [1, 1, 2],
    [0, 1, 1]
])

print("Matrix:\n")

print(A)

# -------------------------------------------------------------
# Rank
# -------------------------------------------------------------
rank = A.rank()

print("\nRank =", rank)

# -------------------------------------------------------------
# Reduced Row Echelon Form
# -------------------------------------------------------------
rref_matrix, pivot_columns = A.rref()

print("\nReduced Row Echelon Form:\n")

print(rref_matrix)

print("\nPivot Columns =", pivot_columns)

# -------------------------------------------------------------
# Linear Independence
# -------------------------------------------------------------
if rank == A.cols:

    print("\nThe vectors are Linearly Independent.")

else:

    print("\nThe vectors are Linearly Dependent.")

# -------------------------------------------------------------
# Basis
# -------------------------------------------------------------
print("\nBasis Vectors:")

for i in pivot_columns:

    print(A.col(i))

print("Basis Vectors:(Method 2)")#easy
print(A.columnspace())

# -------------------------------------------------------------
# Dimension
# -------------------------------------------------------------
print("\nDimension of the Subspace =", rank)