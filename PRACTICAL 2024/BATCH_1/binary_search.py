# Binary Search using User Input

n = int(input("Enter the number of elements: "))

a = []

print("Enter the elements in sorted order:")
for i in range(n):
    a.append(int(input()))

key = int(input("Enter the key value: "))

low = 0
up = len(a) - 1
flag = 0

while low <= up:
    mid = (low + up) // 2

    if key == a[mid]:
        print("Key found at position:", mid)
        flag = 1
        break

    elif key > a[mid]:
        low = mid + 1

    else:
        up = mid - 1

if flag == 0:
    print("Key not found")