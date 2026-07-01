# -------------------------------------------------------------
# Question 9
# Write a Python program to find a pair of indices whose
# corresponding elements add up to a given target value.
# Stop after finding the first solution.
# -------------------------------------------------------------

numbers = [10, 30, 20, 40, 50, 60, 70]

target = int(input("Enter target value: "))

found = False

for i in range(len(numbers)):

    for j in range(i + 1, len(numbers)):

        if numbers[i] + numbers[j] == target:

            print("Index Pair:", i, j)

            found = True
            break

    if found:
        break

if not found:
    print("No Solution Found")