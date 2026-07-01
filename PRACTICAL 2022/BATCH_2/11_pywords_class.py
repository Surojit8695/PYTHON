# -------------------------------------------------------------
# Question 10
# Write a class PyWords with the following functions:
# (a) words_with_length(l)
# (b) starts_with(s)
# (c) palindromes()
# -------------------------------------------------------------

class PyWords:

    def __init__(self, words):
        self.process_words = words

    # Return words of given length
    def words_with_length(self, l):

        result = []

        for word in self.process_words:

            if len(word) == l:
                result.append(word)

        return result

    # Return words starting with given letter
    def starts_with(self, s):

        result = []

        for word in self.process_words:

            if word.startswith(s):
                result.append(word)

        return result

    # Return palindrome words
    def palindromes(self):

        result = []

        for word in self.process_words:

            if word == word[::-1]:
                result.append(word)

        if len(result) == 0:
            return "No palindrome exists."

        return result


# Driver Program
words = input("Enter words separated by space: ").split()

obj = PyWords(words)

length = int(input("Enter length: "))
letter = input("Enter starting letter: ")

print("Words of Length", length, ":", obj.words_with_length(length))
print("Words Starting with", letter, ":", obj.starts_with(letter))
print("Palindromes:", obj.palindromes())