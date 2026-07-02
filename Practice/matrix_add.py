row1=int(input("Enter the size of row:"))
col1=int(input("Enter the size of column:"))
matrix1=[]
for i in range(row1):
    row=[]
    for j in range(col1):
        k=int(input())
        row.append(k)

    matrix1.append(row)

# Print result
for i in matrix1:
    print(i)

# print(matrix1)

row2=int(input("Enter the size of row2:"))
col2=int(input("Enter the size of column2:"))
matrix2=[]
for i in range(row2):
    row=[]
    for j in range(col2):
        k=int(input())
        row.append(k)

    matrix2.append(row)

# Print result
for i in matrix2:
    print(i)


matrix3=[]
for i in range(row1):
    row=[]
    for j in range(col1):
        row.append(matrix1[i][j]+matrix2[i][j])

    matrix3.append(row)

    # Print result
for i in matrix3:
    print(i)