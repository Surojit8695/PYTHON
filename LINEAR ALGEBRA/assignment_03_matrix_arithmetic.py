# -------------------------------------------------------------
# Assignment 3
#
# Question 3
# Write a menu driven program that inputs two matrices
# A and B and perform the following operations:
#
# 1. Addition
# 2. Subtraction
# 3. Multiplication
# 4. Division
#
# Hint:
# Use np.add(), np.subtract(), np.matmul()
# and np.linalg.inv() for matrix operations.
# -------------------------------------------------------------

import numpy as np

# Input matrix size
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("\nEnter elements of Matrix A:")

A = []

for i in range(rows):
    row = list(map(float, input().split()))
    A.append(row)

A = np.array(A)

print("\nEnter elements of Matrix B:")

B = []

for i in range(rows):
    row = list(map(float, input().split()))
    B.append(row)

B = np.array(B)

while True:

    print("\n========== MATRIX MENU ==========")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    # Addition
    if choice == 1:

        result = np.add(A, B)

        print("\nAddition:\n", result)

    # Subtraction
    elif choice == 2:

        result = np.subtract(A, B)

        print("\nSubtraction:\n", result)

    # Multiplication
    elif choice == 3:

        if A.shape[1] != B.shape[0]:

            print("Matrix multiplication is not possible.")

        else:

            result = np.matmul(A, B)

            print("\nMultiplication:\n", result)

    # Division
    elif choice == 4:

        # Division is only possible for square and invertible matrix B
        if B.shape[0] != B.shape[1]:

            print("Division is not possible because Matrix B is not square.")

        elif np.linalg.det(B) == 0:

            print("Division is not possible because Matrix B is singular (determinant = 0).")

        else:

            inverse = np.linalg.inv(B)

            result = np.matmul(A, inverse)

            print("\nDivision (A × B⁻¹):\n", result)

    # Exit
    elif choice == 5:

        print("Program Terminated.")

        break

    else:

        print("Invalid Choice!")