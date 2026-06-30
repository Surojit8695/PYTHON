s=input("Enter the string:")
vowel="aeiouAEIOU"
for ch in s:
    #print(ch)
    if ch  not in vowel and ch.isalpha():
        print(ch)