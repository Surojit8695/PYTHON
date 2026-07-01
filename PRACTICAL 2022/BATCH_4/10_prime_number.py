# -------------------------------------------------------------
# Question 5(b)
# Write a Python program to check whether a number is prime.
# -------------------------------------------------------------

number = int(input("Enter a number: "))

if number < 2:

    print(number, "is not a Prime Number.")

else:

    prime = True

    for i in range(2, int(number ** 0.5) + 1):

        if number % i == 0:
            prime = False
            break

    if prime:
        print(number, "is a Prime Number.")

    else:
        print(number, "is not a Prime Number.")