# Question 4
# Let u = (1,2,3) and v = (4,-1,2) be vectors in R³.
#
# Perform the following operations:
# 1. Vector Addition
# 2. Scalar Multiplication (2u)
# 3. Dot Product
# 4. Orthogonality Check
# 5. Verify the Cauchy–Schwarz Inequality
#
# Hint:
# Use np.array(), np.dot(), and np.linalg.norm().
# -------------------------------------------------------------

import numpy as np

# Given vectors
u = np.array([1, 2, 3])

v = np.array([4, -1, 2])

# -------------------------------
# Vector Addition
# -------------------------------
addition = u + v

print("Vector Addition (u + v):")
print(addition)

# -------------------------------
# Scalar Multiplication
# -------------------------------
scalar = 2

scalar_result = scalar * u

print("\nScalar Multiplication (2u):")
print(scalar_result)

# -------------------------------
# Dot Product
# -------------------------------
dot_product = np.dot(u, v)

print("\nDot Product:")
print(dot_product)

# -------------------------------
# Orthogonality Check
# -------------------------------
if dot_product == 0:

    print("\nVectors are Orthogonal.")

else:

    print("\nVectors are NOT Orthogonal.")

# -------------------------------
# Cauchy–Schwarz Inequality
# -------------------------------
norm_u = np.linalg.norm(u)#magnitude

norm_v = np.linalg.norm(v)

left = abs(dot_product)

right = norm_u * norm_v

print("\n|u·v| =", left)

print("||u|| x ||v|| =", right)

if left <= right:

    print("\nCauchy-Schwarz Inequality is VERIFIED.")

else:

    print("\nCauchy-Schwarz Inequality is NOT VERIFIED.")