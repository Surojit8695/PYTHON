# Function for input the matrix
def input_Matrix(row, col):
    matrix = []
    for i in range(row):
        new = []
        for j in range(col):
            val = int(input())
            new.append(val)
        matrix.append(new)
    return matrix


# Function for display the matrix
def display_Matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j], end="  ")
        print()


# Function for multiplication
def multiply_Matrix(matrix1, matrix2):
    # Condition check
    if len(matrix1[0]) != len(matrix2):
        print("Matrix multiplication not possible")
        return None

    result = []

    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            sum = 0
            for k in range(len(matrix2)):
                sum =sum+( matrix1[i][k] * matrix2[k][j])
            row.append(sum)
        result.append(row)

    return result


#main program
r1 = int(input("Enter rows for 1st matrix: "))
c1 = int(input("Enter cols for 1st matrix: "))
a = input_Matrix(r1, c1)

print("First Matrix:")
display_Matrix(a)

r2 = int(input("\nEnter rows for 2nd matrix: "))
c2 = int(input("Enter cols for 2nd matrix: "))
b = input_Matrix(r2, c2)

print("Second Matrix:")
display_Matrix(b)

result = multiply_Matrix(a, b)

if result is not None:
    print("\nMultiplication Matrix:")
    display_Matrix(result)
