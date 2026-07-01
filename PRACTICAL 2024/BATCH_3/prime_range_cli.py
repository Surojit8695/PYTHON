# Program 3
# Write a Python program to take range of integers
# as command line arguments.
# (a) Display count of non-prime numbers.
# (b) Display list of prime numbers.

import sys

if len(sys.argv) != 3:
    print("Usage: python prime_range_cli.py start end")
    exit()

start = int(sys.argv[1])
end = int(sys.argv[2])

prime_list = []

for num in range(start, end + 1):

    if num < 2:
        continue

    prime = True

    for i in range(2, int(num ** 0.5) + 1):

        if num % i == 0:
            prime = False
            break

    if prime:
        prime_list.append(num)

total = end - start + 1
non_prime = total - len(prime_list)

print("Prime Numbers:", prime_list)
print("Count of Non-Prime Numbers:", non_prime)