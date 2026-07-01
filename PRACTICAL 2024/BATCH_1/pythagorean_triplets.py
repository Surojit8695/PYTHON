# Program 3
# Write a Python program to generate all Pythagorean Triplets
# whose values are less than or equal to the given limit.
limit = int(input("Enter the limit: "))

print("Pythagorean Triplets are:")

for a in range(1, limit + 1):
    for b in range(a + 1, limit + 1):
        for c in range(b + 1, limit + 1):
            if a*a + b*b == c*c:
                print(a, b, c)



# for i in range(1, limit + 1):
#     for j in range(i + 1, limit + 1):
#         k = (i*i + j*j) ** 0.5

#         if k == int(k) and k <= limit:
#             print(i, j, int(k))