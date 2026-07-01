# -------------------------------------------------------------
# Question 2
# Read the given dictionary and print:
# (a) Users whose phone number ends in 5
# (b) Users without email address
# (c) Users whose phone number starts with 9
# -------------------------------------------------------------

users = [

    {"name": "Ram",
     "phone": "9434141414",
     "email": "ram@gmail.com"},

    {"name": "Laksman",
     "phone": "8434151515",
     "email": ""},

    {"name": "Bharat",
     "phone": "7474161616",
     "email": "bharat@gmail.com"},

    {"name": "Satrughna",
     "phone": "9478171717",
     "email": "satrughna@gmail.com"}

]

print("Phone number ends with 5")

for user in users:

    if user["phone"].endswith("5"):
        print(user["name"])

print("\nUsers without email")

for user in users:

    if user["email"] == "":
        print(user["name"])

print("\nPhone number starts with 9")

for user in users:

    if user["phone"].startswith("9"):
        print(user["name"])