n = int(input("Enter the number of rows: "))
for i in range(0, n ):
    ch=65
    print(" " * (n-i), end=" ")

    # Print stars (range stops right before 2*i)
    for k in range(0, i +1):
        print(chr(ch), end=" ")
        ch=ch+1
    print()
