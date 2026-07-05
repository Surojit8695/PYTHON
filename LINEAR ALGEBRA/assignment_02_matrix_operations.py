# -------------------------------------------------------------
# Assignment 2
#
# Question 2
# Write a program that inputs a square matrix of order N
# and perform the following operations:
#
# 1. Determinant
# 2. Inverse
# 3. Transpose
# 4. Scalar Multiplication
# 5. Adjoint
# 6. Rank
# 7. Diagonal Elements
# 8. Trace
# 9. Eigenvalues
# 10. Eigenvectors
#
# Hint:
# Use np.linalg.det(), np.linalg.inv(),
# np.linalg.eig(), np.linalg.matrix_rank()
# -------------------------------------------------------------

import numpy as np

# Input order of square matrix
n = int(input("Enter the order of the square matrix: "))

print("Enter the matrix elements:")

matrix = []

for i in range(n):
    row = list(map(float, input().split()))
    matrix.append(row)

A = np.array(matrix)

while True:

    print("\n========== MATRIX MENU ==========")
    print("1. Determinant")
    print("2. Inverse")
    print("3. Transpose")
    print("4. Scalar Multiplication")
    print("5. Adjoint")
    print("6. Rank")
    print("7. Diagonal Elements")
    print("8. Trace")
    print("9. Eigenvalues")
    print("10. Eigenvectors")
    print("11. Exit")

    choice = int(input("Enter your choice: "))

    # Determinant
    if choice == 1:

        print("Determinant =", np.linalg.det(A))

    # Inverse
    elif choice == 2:

        if np.linalg.det(A) == 0:

            print("Inverse does not exist.")

        else:

            print("Inverse Matrix:\n", np.linalg.inv(A))

    # Transpose
    elif choice == 3:

        print("Transpose:\n", A.T)

    # Scalar Multiplication
    elif choice == 4:

        scalar = float(input("Enter scalar value: "))

        print("Result:\n", scalar * A)

    # Adjoint
    elif choice == 5:

        if np.linalg.det(A) == 0:

            print("Adjoint cannot be calculated using inverse because the matrix is singular.")

        else:

            adj = np.linalg.det(A) * np.linalg.inv(A)

            print("Adjoint Matrix:\n", adj)

    # Rank
    elif choice == 6:

        print("Rank =", np.linalg.matrix_rank(A))

    # Diagonal Elements
    elif choice == 7:

        print("Diagonal Elements =", np.diag(A))

    # Trace
    elif choice == 8:

        print("Trace =", np.trace(A))

    # Eigenvalues
    elif choice == 9:

        values, vectors = np.linalg.eig(A)

        print("Eigenvalues:\n", values)

    # Eigenvectors
    elif choice == 10:

        values, vectors = np.linalg.eig(A)

        print("Eigenvectors:\n", vectors)

    # Exit
    elif choice == 11:

        print("Program Terminated.")

        break

    else:

        print("Invalid Choice!")
