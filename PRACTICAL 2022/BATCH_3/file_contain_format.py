file1 = "C:\\Users\\suroj\\OneDrive\\Desktop\\PYTHON\\PRACTICAL 2022\\matter.txt"

fp = open(file1, "r")
data = fp.read()
fp.close()

result = ""

for i in range(len(data)):

    if data[i].isalnum():

        # If next character exists and is a space
        if i < len(data)-1 and data[i+1] == " ":
            result += data[i]

        else:
            result += data[i] + "#"

    elif data[i] == " ":
        result += "$"

print(result)