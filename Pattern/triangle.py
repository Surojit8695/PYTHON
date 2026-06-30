n = int(input("Enter the number of rows: "))
for i in range(1, n + 1):
    ch=65
    # Print leading spaces
    for j in range(0,n - i):
        print(" ", end=" ")

    # Print stars (range stops right before 2*i)
    for k in range(0, 2 * i-1):
        print(chr(ch), end=" ")
        ch=ch+1
    print()
