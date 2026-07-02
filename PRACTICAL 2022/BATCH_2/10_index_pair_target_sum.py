# -------------------------------------------------------------
# Question 9
# Write a Python program to find a pair of indices whose
# corresponding elements add up to a given target value.
# Stop after finding the first solution.
# -------------------------------------------------------------

numbers = [10, 20, 30, 40, 50, 60, 70]

target = int(input("Enter target value: "))

flag = 0

for i in range(len(numbers)):

    for j in range(i + 1, len(numbers)):

        if numbers[i] + numbers[j] == target:

            print("Index Pair:", i, j)
            flag=1


if flag == 0:
    print("No Solution Found")

# output:    
# Enter target value: 50
# Index Pair: 0 3 <-------(10+40)
# Index Pair: 1 2  <-------(20+30)
# output:
# Index Pair: 0 5
# Index Pair: 1 4
# Index Pair: 2 3