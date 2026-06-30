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


# Function for diagonal sum
def diagonal_sum(matrix):
    n = len(matrix)

    # Check square matrix
    if n != len(matrix[0]):
        print("Diagonal sum only possible for square matrix")
        return None

    primary = 0
    secondary = 0

    for i in range(n):
        primary += matrix[i][i]              # main diagonal
        secondary += matrix[i][n-i-1]       # secondary diagonal

    return primary, secondary


#main program
r = int(input("Enter number of rows: "))
c = int(input("Enter number of columns: "))

a = input_Matrix(r, c)

print("\nMatrix:")
display_Matrix(a)

result = diagonal_sum(a)

if result is not None:
    print("\nPrimary Diagonal Sum:", result[0])
    print("Secondary Diagonal Sum:", result[1])
