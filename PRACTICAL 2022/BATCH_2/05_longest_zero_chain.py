# -------------------------------------------------------------
# Question 5
# Populate a list with 0 and 1.
# Find the longest chain of zeros and its index span.
# -------------------------------------------------------------

numbers = list(map(int, input("Enter 0s and 1s separated by space: ").split()))

max_count = 0
current_count = 0

start = 0
end = 0

temp_start = 0

for i in range(len(numbers)):

    if numbers[i] == 0:

        if current_count == 0:
            temp_start = i

        current_count += 1

        if current_count > max_count:

            max_count = current_count

            start = temp_start
            end = i

    else:

        current_count = 0

print("Longest chain of zeros =", max_count)

if max_count > 0:
    print("Span =", start, "to", end)
else:
    print("No zero chain found.")