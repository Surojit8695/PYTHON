# 3. Given a string write a program in Python to find the occurrences of every character, number, special
# character, punctuations etc. 
s=input("Enter the string:")
frequency={}
for ch in s:
    if ch in frequency:
        frequency[ch]+=1
    else:
        frequency[ch]=1
# print(frequency)
for key,value in frequency.items():
    print(key,":",value)

digit=0
letter=0
special=0
punctuation=0
space=0
for ch in s:
    if ch.isalpha():
        letter+=1
    elif ch.isdigit():
        digit+=1
    elif ch.isspace():
        space+=1
    elif ch in ".,?!":
        punctuation+=1
    else:
        special+=1
print("\nSummary")
print("Letters      :", letter)
print("Digits       :", digit)
print("Punctuations :", punctuation)
print("Spaces       :", space)
print("Special Char :", special)

