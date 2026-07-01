# -------------------------------------------------------------
# Question 8
# Write a Python program to implement Quick Sort.
# -------------------------------------------------------------

# Quick Sort Function
def quick_sort(arr):

    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]

    left = []
    middle = []
    right = []

    for x in arr:

        if x < pivot:
            left.append(x)

        elif x == pivot:
            middle.append(x)

        else:
            right.append(x)

    return quick_sort(left) + middle + quick_sort(right)


# Driver Program
numbers = list(map(int, input("Enter list elements: ").split()))

print("Sorted List =", quick_sort(numbers))