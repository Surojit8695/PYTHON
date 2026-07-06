# Question 1
# Write a menu driven program that inputs 2 vectors u and v
# of dimension 3 and perform the following operations:
#
# 1. Vector Addition
# 2. Scalar Multiplication
# 3. Dot Product
# 4. Cross Product
# 5. Orthogonality Check
# 6. Parallelism Check
#
# Hint:
# Use np.array for input and np.dot(), np.cross(),
# and np.linalg.norm() for calculations.
# -------------------------------------------------------------

import numpy as np

# Taking input for first vector
print("Enter the elements of Vector U:")
u = np.array(list(map(float, input().split())))

# Taking input for second vector
print("Enter the elements of Vector V:")
v = np.array(list(map(float, input().split())))

while True:

    print("\n========== VECTOR MENU ==========")
    print("1. Vector Addition")
    print("2. Scalar Multiplication")
    print("3. Dot Product")
    print("4. Cross Product")
    print("5. Orthogonality Check")
    print("6. Parallelism Check")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    # Vector Addition
    if choice == 1:

        result = u + v

        print("Vector Addition =", result)

    # Scalar Multiplication
    elif choice == 2:

        scalar = float(input("Enter scalar value: "))

        print(f"Scalar {scalar} U =", scalar * u)

        print(f"Scalar {scalar} V =", scalar * v)

    # Dot Product
    elif choice == 3:

        result = np.dot(u, v)

        print("Dot Product =", result)

    # Cross Product
    elif choice == 4:

        result = np.cross(u, v)

        print("Cross Product =", result)

    # Orthogonality Check
    elif choice == 5:

        if np.dot(u, v) == 0:

            print("Vectors are Orthogonal.")

        else:

            print("Vectors are NOT Orthogonal.")

    # Parallelism Check
    elif choice == 6:

        cross = np.cross(u, v)

        if np.linalg.norm(cross) == 0:

            print("Vectors are Parallel.")

        else:

            print("Vectors are NOT Parallel.")

    # Exit
    elif choice == 7:

        print("Program Terminated.")

        break

    else:

        print("Invalid Choice!")