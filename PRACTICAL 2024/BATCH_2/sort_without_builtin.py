# Program 4
# Write a Python program to sort a list without using
# built-in sort() function.
# Sort only if there are no duplicate elements.

numbers = list(map(int, input("Enter list elements: ").split()))

duplicate = False

for i in range(len(numbers)):
    if numbers.count(numbers[i]) > 1:
        duplicate = True
        break

if duplicate:
    print("Duplicate element found. Sorting not allowed.")

else:

    for i in range(len(numbers)):

        for j in range(i + 1, len(numbers)):

            if numbers[i] > numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]

    print("Sorted List:", numbers)