limit = int(input("Enter the limit: "))

fib = [0, 1]

while fib[-1] < limit:
    fib.append(fib[-1] + fib[-2])

print("Non-Fibonacci numbers:")

for i in range(limit + 1):
    if i not in fib:
        print(i, end=" ")




#method 2
while True:
    print("\n----- MENU -----")
    print("1. Print Non-Fibonacci Sequence")
    print("2. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        n = int(input("Enter the number of terms: "))

        a = 1
        b = 2
        count = 0

        print("Non-Fibonacci Sequence:")

        while count < n:
            for i in range(a + 1, b):
                print(i, end=" ")
                count += 1
                if count == n:
                    break

            c = a + b
            a = b
            b = c

        print()

    elif choice == 2:
        print("Program Exited.")
        break

    else:
        print("Invalid Choice")