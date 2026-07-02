# Program 3
# Write a menu driven Python program that prints
# the Non-Fibonacci sequence up to Nth term.

def generate_non_fibonacci(n):

    a = 1
    b = 2
    count = 0

    while count < n:

        for i in range(a + 1, b):

            if count == n:
                break
 
            print(i, end=" ")
            count += 1

        a = b
        b = a + b


while True:

    print("\n1. Generate Non-Fibonacci")
    print("2. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        n = int(input("Enter number of terms: "))
        generate_non_fibonacci(n)
        print()

    elif choice == 2:
        break

    else:
        print("Invalid Choice")