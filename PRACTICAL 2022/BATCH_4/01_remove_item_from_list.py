# -------------------------------------------------------------
# Question 1(a)
# Write a Python function to remove all occurrences of a given
# item from a list.
# -------------------------------------------------------------

# Function to remove all occurrences
# def remove_item(lst, item):

#     while item in lst:
#         lst.remove(item)

#     return lst


# # Driver Program
# numbers = list(map(int, input("Enter list elements: ").split()))

# item = int(input("Enter item to remove: "))

# print("Updated List:", remove_item(numbers, item))

##method 2
numbers = list(map(int, input("Enter list elements: ").split()))
item = int(input("Enter item to remove: "))

new_list = []

for i in numbers:
    if i != item:
        new_list.append(i)

print("Updated List:", new_list)