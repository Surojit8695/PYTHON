# nie a program in Python to use the file data.txt for solving and displaying outputs the following tasks
# after reading it:
# (a) All words ending with "on"
# (b) All words whose second and third letters are "" and "c"
# (c) All words with no vowels. 

file1="C:\\Users\\suroj\\OneDrive\\Desktop\\PYTHON\\PRACTICAL 2022\\BATCH_2\\input.txt"
fp=open(file1,"r")
data=fp.read().split()
fp.close()
print("words ending with on:")
for word in data:
    if word.endswith("on"):
        print(word)
print("words with re in 2nd and 3rd position:")
for word in data:
    if len(word) >= 3 and word[1:3] == "re":
        print(word)
#all words with no vowels
print("words with no vowels:")
for word in data:
    if ('a' not in word.lower() and
        'e' not in word.lower() and
        'i' not in word.lower() and
        'o' not in word.lower() and
        'u' not in word.lower()):
        print(word)