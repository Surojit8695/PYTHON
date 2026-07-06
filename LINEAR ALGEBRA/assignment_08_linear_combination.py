# Question 8
# Write a Python program that inputs N vectors of dimension 3
# and corresponding scalars.
#
# Compute the linear combination:
#
# a1u1 + a2u2 + ... + aNuN
#
# Check whether the resulting vector is the zero vector.
# Comment whether the vectors may be linearly dependent.
# -------------------------------------------------------------

import numpy as np

# -------------------------------------------------------------
# Input number of vectors
# -------------------------------------------------------------
n = int(input("Enter the number of vectors: "))

vectors = []
scalars = []

# -------------------------------------------------------------
# Input vectors and scalars
# -------------------------------------------------------------
for i in range(n):

    print(f"\nEnter Vector {i+1} (3 elements):")

    u1 = np.array(list(map(float, input().split())))

    vectors.append(u1)

    scalar = float(input(f"Enter Scalar a{i+1}: "))

    scalars.append(scalar)

# -------------------------------------------------------------
# Compute Linear Combination
# -------------------------------------------------------------
result = np.zeros(3)#The function np.zeros() creates a NumPy array filled with zeros.
#It is commonly used to initialize an array before storing values in it.

for i in range(n):

    result = result + scalars[i] * vectors[i]

# -------------------------------------------------------------
# Display Result
# -------------------------------------------------------------
print("\nLinear Combination =")

print(result)

# -------------------------------------------------------------
# Check Zero Vector
# -------------------------------------------------------------
if np.all(result == 0):

    print("\nResult is the Zero Vector.")

    print("The given vectors may be Linearly Dependent.")

else:

    print("\nResult is NOT the Zero Vector.")

    print("The vectors are not proven to be linearly dependent.")