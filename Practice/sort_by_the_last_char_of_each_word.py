words = ["apple", "banana", "mango", "kiwi"]

words.sort(key=lambda x: x[-1])

print(words)


# ##Without lambda
# def last_character(word):
#     return word[-1]

# words = ["apple", "banana", "mango", "kiwi"]

# words.sort(key=last_character)

# print(words)