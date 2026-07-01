# Program 2
# Write a Python program to validate passwords.
# Conditions:
# 1. At least one lowercase letter
# 2. At least one uppercase letter
# 3. At least one digit
# 4. At least one special character from [$#@]
# 5. Length between 6 and 12
n = int(input("Enter the Number of Passwords: "))

print("Enter the set of passwords:")

psw = []
valid=[]

for i in range(n):
    psw.append(input(f"Enter Password {i+1}:"))

for p in psw:#surojit@123

    lower = upper = digit = special = 0

    if len(p) >= 6 and len(p) <= 12:

        for ch in p:
            if ch.islower():
                lower = 1
            elif ch.isupper():
                upper = 1
            elif ch.isdigit():
                digit = 1
            elif ch in "$#@":
                special = 1

        if lower and upper and digit and special:
            valid.append(p)

print(",".join(valid))
#print(valid)