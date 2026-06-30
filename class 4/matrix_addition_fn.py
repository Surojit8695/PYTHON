#Function for input the matrix
def input_Matrix(row,col):
    matrix=[]
    for i in range(row):
        new=[]
        for j in range(col):
            val=int(input())
            new.append(val)
        matrix.append(new)
    return matrix

#Function for display the matrix
def display_Matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j],end="  ")
        print()

#function for addition the matrix
def add_Matrix(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        print( "Matrix addition not possible (different sizes)")
        return None
    
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    
    return result

r1=int(input("Enter the row number for 1st matrix:"))
c1=int(input("Enter the col number for 1st matrix:"))
a=input_Matrix(r1,c1)
print("The first matrix is:")
display_Matrix(a)

r2=int(input("Enter the row number for 2nd matrix:"))
c2=int(input("Enter the col number for 2nd matrix:"))
b=input_Matrix(r2,c2)
print("The second matrix is:")
display_Matrix(b)

result=add_Matrix(a,b)
if result is not None:
    print("\nAddition Matrix:")
    display_Matrix(result)
