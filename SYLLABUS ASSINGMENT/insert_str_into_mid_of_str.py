# Function to insert a string in the middle

def insert_middle(s1, s2):
    middle = len(s1) // 2
    result = s1[:middle] + s2 + s1[middle:]
    return result

str1 = input("Enter the original string: ")
str2 = input("Enter the string to insert: ")

print("Result:", insert_middle(str1, str2))