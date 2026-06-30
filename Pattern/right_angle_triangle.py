n = int(input("Enter the number of rows: "))
k=1
for i in range(n, 0,-1):
    for j in range(1, i+1):
        print("*", end=" ")
        k=k+1
    print()

