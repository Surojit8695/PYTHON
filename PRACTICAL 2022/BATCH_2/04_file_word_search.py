# -------------------------------------------------------------
# Question 4
# Read data.txt and display:
# (a) Words ending with "on"
# (b) Words whose 2nd and 3rd letters are 't' and 'e'
# (c) Words with no vowels
# -------------------------------------------------------------

# Open file
file = open("data.txt", "r")

text = file.read()

file.close()

words = text.split()

print("Words ending with 'on'")

for word in words:

    if word.endswith("on"):
        print(word)

print("\nSecond and third letters are 't' and 'e'")

for word in words:

    if len(word) >= 3 and word[1] == 't' and word[2] == 'e':
        print(word)

print("\nWords without vowels")

for word in words:

    vowel = False

    for ch in word.lower():

        if ch in "aeiou":
            vowel = True
            break

    if not vowel:
        print(word)