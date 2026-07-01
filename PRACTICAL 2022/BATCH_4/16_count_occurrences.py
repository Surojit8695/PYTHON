# -------------------------------------------------------------
# Question 9(b)
# Write a Python program to get the number of occurrences
# of a specified element in an array.
# -------------------------------------------------------------

numbers = list(map(int, input("Enter array elements: ").split()))

element = int(input("Enter element to count: "))

count = 0

for num in numbers:

    if num == element:
        count += 1

print("Occurrences =", count)