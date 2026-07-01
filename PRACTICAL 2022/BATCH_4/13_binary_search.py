# -------------------------------------------------------------
# Question 7
# Write a Python program to implement Binary Search.
# -------------------------------------------------------------

numbers = list(map(int, input("Enter sorted list elements: ").split()))

key = int(input("Enter element to search: "))

low = 0
high = len(numbers) - 1

found = False

while low <= high:

    mid = (low + high) // 2

    if numbers[mid] == key:

        print("Element Found at Index", mid)
        found = True
        break

    elif numbers[mid] < key:
        low = mid + 1

    else:
        high = mid - 1

if not found:
    print("Element Not Found")