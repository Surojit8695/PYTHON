# -------------------------------------------------------------
# Question:
# Write a program in Python that fills an empty list with n integers,
# where n is user input. Then find the longest chain of
# monotonically ascending or descending values.
# User chooses ascending or descending.
# Print "NIL" if no such chain exists.
# -------------------------------------------------------------

n = int(input("Enter number of elements: "))

lst = []

print("Enter elements:")

for i in range(n):
    lst.append(int(input()))

choice = input("Enter choice (ascending/descending): ").lower()

longest = []
current = [lst[0]]

for i in range(1, len(lst)):

    if choice == "ascending":
        if lst[i] >= lst[i-1]:
            current.append(lst[i])
        else:
            if len(current) > len(longest):
                longest = current
            current = [lst[i]]

    elif choice == "descending":
        if lst[i] <= lst[i-1]:
            current.append(lst[i])
        else:
            if len(current) > len(longest):
                longest = current
            current = [lst[i]]

if len(current) > len(longest):
    longest = current

if len(longest) <= 1:
    print("NIL")
else:
    print("Longest Chain:", longest)