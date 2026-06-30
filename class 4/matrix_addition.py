# Matrix Addition

r = int(input("Enter the row size: "))
c = int(input("Enter the column size: "))

# First matrix
a = []
print("Enter the elements of first matrix:")
for i in range(r):
    row = []
    for j in range(c):
        k = int(input())
        row.append(k)
    a.append(row)

# Second matrix
b = []
print("Enter the elements of second matrix:")
for i in range(r):
    row = []
    for j in range(c):
        k = int(input())
        row.append(k)
    b.append(row)

# Addition
result = []
print("Addition of two matrix is:")
for i in range(r):
    row = []
    for j in range(c):
        row.append(a[i][j] + b[i][j])
    result.append(row)

# Print result
for i in result:
    print(i)
