# -------------------------------------------------------------
# Question 4(a)
# Write a Python program to count Even and Odd numbers
# in a list.
# -------------------------------------------------------------

numbers = list(map(int, input("Enter list elements: ").split()))

even = 0
odd = 0

for num in numbers:

    if num % 2 == 0:
        even += 1

    else:
        odd += 1

print("Even Count =", even)

print("Odd Count =", odd)