# -------------------------------------------------------------
# Question 2
# Write a Python program to print all non-prime,
# non-Fibonacci numbers within range a-b.
# -------------------------------------------------------------

import sys

# Check command line arguments
if len(sys.argv) != 3:
    print("Usage: python 02_nonprime_nonfibonacci.py start end")
    exit()

a = int(sys.argv[1])
b = int(sys.argv[2])


# Function to check prime
def is_prime(n):

    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


# Function to check Fibonacci
def is_fibonacci(n):

    x = 0
    y = 1

    while y < n:
        x, y = y, x + y

    return n == 0 or y == n


print("Non-prime and Non-Fibonacci Numbers:")

for i in range(a, b + 1):

    if (not is_prime(i)) and (not is_fibonacci(i)):
        print(i, end=" ")