str1=input("Enter the string:")
result=""
for ch in str1:
    if ch not in "aeiouAEIOU":
        result=result+ch
print("The string after removing vowel is:",result)

'''
s = input("Enter a string: ")

for ch in "aeiouAEIOU":
    s = s.replace(ch, "")

print("String after removing vowels:", s)
'''