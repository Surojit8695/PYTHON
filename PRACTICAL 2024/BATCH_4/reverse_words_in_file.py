# 2. Write a Python program to reverse each word in text file taken as input.
file1="C:\\Users\\suroj\\OneDrive\\Desktop\\PYTHON\\PRACTICAL 2024\\BATCH_4\\text.txt"
fp = open(file1, "r")
data = fp.read()
r=data.split()
print(r)
for wrd in r:
    print(wrd[::-1])

fp.close()