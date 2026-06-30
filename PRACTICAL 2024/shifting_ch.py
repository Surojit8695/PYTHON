s=input("Enter the string:")
shift=int(input("Enter the shifting beat:"))
result=""
for ch in s:
    # print(ch)
    if ch.isupper():
        k=chr((ord(ch)+shift-65)%26+65)
        result+=k
    elif ch.islower():
        k=chr((ord(ch)+shift-97)%26+97)
        result+=k
    
print(result)