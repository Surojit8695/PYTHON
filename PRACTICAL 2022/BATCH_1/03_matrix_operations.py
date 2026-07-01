# -------------------------------------------------------------
# Question 3
# Write a Python program to perform matrix addition,
# subtraction and multiplication using list of lists.
# -------------------------------------------------------------

# Function for matrix addition
def add_matrix(A, B):

    result = []

    for i in range(len(A)):

        row = []

        for j in range(len(A[0])):
            row.append(A[i][j] + B[i][j])

        result.append(row)

    return result


# Function for matrix subtraction
def subtract_matrix(A, B):

    result = []

    for i in range(len(A)):

        row = []

        for j in range(len(A[0])):
            row.append(A[i][j] - B[i][j])

        result.append(row)

    return result


# Function for matrix multiplication
def multiply_matrix(A, B):

    result = []

    for i in range(len(A)):

        row = []

        for j in range(len(B[0])):

            total = 0

            for k in range(len(B)):
                total += A[i][k] * B[k][j]

            row.append(total)

        result.append(row)

    return result


# Input matrix size
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("Enter First Matrix")

A = []

for i in range(rows):
    A.append(list(map(int, input().split())))

print("Enter Second Matrix")

B = []

for i in range(rows):
    B.append(list(map(int, input().split())))

print("\nAddition")
print(add_matrix(A, B))

print("\nSubtraction")
print(subtract_matrix(A, B))

print("\nMultiplication")
print(multiply_matrix(A, B))