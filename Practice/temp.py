file1="C:\\Users\\suroj\\OneDrive\\Desktop\\PYTHON\\Practice\\input.txt"
fp=open(file1,"r")
data=fp.read().split()
print("words ending with on:")
for i in data:
    if i.endswith("on"):
        print(i)
print("words with re in 2nd and 3rd position:")
for i in data:
    if i[2:4]=="re":
        print(i)
#all words with no vowels
print("words with no vowels:")
for word in data:

    if ('a' not in word and
        'e' not in word and
        'i' not in word and
        'o' not in word and
        'u' not in word):

        print(word)