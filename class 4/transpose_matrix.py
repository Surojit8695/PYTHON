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


# Function for transpose
def transpose_Matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    result = []

    for j in range(cols):      # column becomes row
        row = []
        for i in range(rows):
            row.append(matrix[i][j])
        result.append(row)

    return result


#main program
r = int(input("Enter number of rows: "))
c = int(input("Enter number of columns: "))

a = input_Matrix(r, c)

print("\nOriginal Matrix:")
display_Matrix(a)

t = transpose_Matrix(a)

print("\nTranspose Matrix:")
display_Matrix(t)
