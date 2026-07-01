# -------------------------------------------------------------
# Question 7(a)
# Write a Python program to find all numbers between 1 and N
# that are divisible by 7 and end in 6.
# Also display their count.
# -------------------------------------------------------------

N = int(input("Enter the value of N: "))

count = 0

print("Numbers are:")

for i in range(1, N + 1):

    if i % 7 == 0 and i % 10 == 6:
        print(i, end=" ")
        count += 1

print("\nCount =", count)