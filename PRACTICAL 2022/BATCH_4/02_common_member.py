# -------------------------------------------------------------
# Question 1(b)
# Write a Python function that takes two lists and returns
# True if they have at least one common member.
# -------------------------------------------------------------

# Function to check common member
def common_member(list1, list2):

    for item in list1:

        if item in list2:
            return True

    return False

list1 = input("Enter first list elements: ").split()
list2 = input("Enter second list elements: ").split()

print(common_member(list1, list2))

# # method 2
# list1 = input("Enter first list elements: ").split()
# list2 = input("Enter second list elements: ").split()

# set1 = set(list1)
# set2 = set(list2)

# if set1.intersection(set2):
#     print(True)
# else:
#     print(False)