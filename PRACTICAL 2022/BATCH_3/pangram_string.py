# Function to check whether a string is a pangram
# "The quick brown fox jumps over the lazy dog" 
def check_pangram(sentence):

    letters = set()

    for ch in sentence.lower():
        if ch.isalpha():
            letters.add(ch)

    if len(letters) == 26:
        return True
    else:
        return False


# Driver Code
text = input("Enter a sentence: ")

if check_pangram(text):
    print("The given sentence is a Pangram.")
else:
    print("The given sentence is NOT a Pangram.")

# "The quick brown fox jumps over the lazy dog" 