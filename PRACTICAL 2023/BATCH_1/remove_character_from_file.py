# -------------------------------------------------------------
# Question:
# Write a Python function that reads a text file and:
# (a) Accept a character from user.
# (b) If character not found, ask again.
# (c) Remove all occurrences and display remaining contents.
# -------------------------------------------------------------

filename = input("Enter file name: ")

with open(filename, "r") as file:
    text = file.read()

while True:

    ch = input("Enter character to remove: ")

    if ch in text:
        break

    print("Character not found. Enter again.")

new_text = text.replace(ch, "")

print("\nModified Text:\n")
print(new_text)

with open("output.txt", "w") as file:
    file.write(new_text)

print("\nModified content saved in output.txt")