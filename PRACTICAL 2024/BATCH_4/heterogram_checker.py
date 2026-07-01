# 5. Given a string S of lowercase characters, write a program in Python to check whether a given string
# is a Heterogram or not using Python. A heterogram is a word, phrase, or sentence in which no letter
# of the alphabet occurs more than once.
s = input("Enter a string: ")

flag = True

for i in range(len(s)):
    if s[i] in s[i+1:]:#here in operator is there
        flag = False
        break

if flag:
    print("Heterogram")
else:
    print("Not Heterogram")


# # method 2 using set oppearator
# print(set(s))
# if len(s) == len(set(s)):
#    print("Heterogram")
# else:
#      print("Not Heterogram")

