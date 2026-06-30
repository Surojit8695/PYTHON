
# s=input("Enter the string:")
# print(s)
# result=""
# vowel="aeiouAEIOU"
# for ch in s:
#     if ch not in vowel:
#         result=result+ch
# print(result)

#15. Write a function to insert a string in the middle of the string
# def insert_mid(str1,str2):
#     middle=len(str1)//2
#     r=s1[:middle]+str2+s1[middle:]
#     return r

# s1=input("Enter the main string:")
# print(s1)
# s2=input("Enter the second string:")
# print(s2)
# r=insert_mid(s1,s2)
# print(r)

#16. Write a program to sort a string lexicographically.
# s1=input("Enter the string:")
# l1=list(s1)
# l1.sort()
# print(l1)
# p1="".join(l1)
# print(p1)

#17. Write a program to replace a string with another string without using built-in methods.
s=input("Enter the string:")
old=input("Enter the string to replace:")
new=input("Enter the new string:")
result=""
i=0
while i<len(s):
    if s[i:i+len(old)]==old:
        result=result+new
        i=i+len(old)
    else:
        result=result+s[i]
        i=i+1
print(result)

#18. Write a program to concatenate two strings into another string without using the + operator.
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

result = []

for ch in s1:
    result.append(ch)

for ch in s2:
    result.append(ch)

final = "".join(result)

print("Concatenated String:", final)

# Program to strip a set of characters from a string

s = input("Enter a string: ")
chars = input("Enter characters to remove: ")

result = ""

for ch in s:
    if ch not in chars:
        result += ch

print("String after stripping:", result)