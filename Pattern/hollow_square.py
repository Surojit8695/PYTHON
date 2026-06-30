n = int(input("Enter the number of rows: "))

for i in range(0, n):
    for j in range(0, n):
        # 0 targets the first row/column, n-1 targets the last row/column
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
