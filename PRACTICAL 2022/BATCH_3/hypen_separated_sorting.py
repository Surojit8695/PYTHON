# Write a Python program that accepts a hyphen-separated sequence of words as input and prints the
# words in a hyphen-separated sequence after sorting them alphabetically.
# Sample ltems: green-red-yellow-black-white
# Expected Result: black-green-red-white-yellow

input_string = input("Enter hyphen-separated words: ")

word_list = input_string.split("-")

print("Original list of words:")
print(word_list)

word_list.sort()

print("\nSorted list of words:")
print(word_list)

sorted_string = "-".join(word_list)

print("\nHyphen-separated sorted string:")
print(sorted_string)

