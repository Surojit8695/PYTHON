#linear search

def linear_search(arr, key):
    """Performs linear search on array"""
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

# Take user input
n = int(input("Enter number of elements: "))
arr = []
print("Enter elements: ")
for i in range(n):
    element = int(input(f"Element {i+1}: "))
    arr.append(element)

key = int(input("Enter key element to search: "))

result = linear_search(arr, key)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")
