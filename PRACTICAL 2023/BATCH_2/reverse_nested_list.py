# -------------------------------------------------------------
# Question:
# Write a program in Python to implement a function that reverses
# elements of a nested list recursively.
#
# Example:
# Input:
# [[[1, 2], [3, [4, 5]]], 6]
#
# Output:
# [6, [[5, 4], 3], [2, 1]]
# -------------------------------------------------------------

# Recursive function to reverse a nested list
def reverse_nested(lst):

    # If the object is not a list, return it directly
    if not isinstance(lst, list):
        return lst

    # Reverse the list and recursively reverse nested lists
    result = []

    for item in reversed(lst):

        result.append(reverse_nested(item))

    return result


# Example nested list
nested_list = [[[1, 2], [3, [4, 5]]], 6]

print("Original List:")
print(nested_list)

print("\nReversed Nested List:")
print(reverse_nested(nested_list))