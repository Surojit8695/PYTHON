# -------------------------------------------------------------
# Question 2(a)
# Write a Python program to perform the following operations
# on two sets:
# (i) Union
# (ii) Intersection
# (iii) Set Difference
# -------------------------------------------------------------

# Input two sets
set1 = set(input("Enter first set elements: ").split())
set2 = set(input("Enter second set elements: ").split())

print("Union =", set1 | set2)

print("Intersection =", set1 & set2)

print("Difference (Set1 - Set2) =", set1 - set2)