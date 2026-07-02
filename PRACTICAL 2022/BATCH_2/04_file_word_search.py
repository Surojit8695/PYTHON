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
for i in data:
    if i.endswith("on"):
        print(i)
print("words with re in 2nd and 3rd position:")
for i in data:
    if len(i) >= 3 and i[1:3] == "re":
        print(i)
#all words with no vowels
print("words with no vowels:")
for word in data:
    word_lower = word.lower()
    if ('a' not in word_lower and
        'e' not in word_lower and
        'i' not in word_lower and
        'o' not in word_lower and
        'u' not in word_lower):
        print(word)