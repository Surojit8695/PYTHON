# -------------------------------------------------------------
# Question 5
# Write a Python program to input two sets S1 and S2
# containing city names.
#
# (a) Find Union, Intersection and Symmetric Difference.
# (b) Display S1 in uppercase and S2 in lowercase.
# -------------------------------------------------------------

# Input first set
S1 = set(input("Enter cities for Set-1: ").split())

# Input second set
S2 = set(input("Enter cities for Set-2: ").split())

print("Union =", S1 | S2)

print("Intersection =", S1 & S2)

print("Symmetric Difference =", S1 ^ S2)

print("\nSet-1 in Uppercase")

for city in S1:
    print(city.upper())

print("\nSet-2 in Lowercase")

for city in S2:
    print(city.lower())