# -------------------------------------------------------------
# Question 9
# Write a Python program that stores names of 8 batsmen and
# their international runs.
#
# (a) Sort dictionary in descending order of runs.
# (b) Display batsman with maximum runs.
# (c) Display only batsmen names.
# (d) Add a new batsman.
# (e) Remove batsman with lowest runs.
# -------------------------------------------------------------

# Dictionary of batsmen
batsmen = {
    "Sachin": 34357,
    "Virat": 27599,
    "Rohit": 19700,
    "Dhoni": 17092,
    "Dravid": 24208,
    "Ganguly": 18433,
    "Sehwag": 17253,
    "Laxman": 11119
}

# Sort dictionary in descending order
sorted_dict = dict(sorted(batsmen.items(),
                          key=lambda item: item[1],
                          reverse=True))

print("Sorted Dictionary")

for name, runs in sorted_dict.items():
    print(name, ":", runs)

# Batsman with maximum runs
maximum = max(batsmen, key=batsmen.get)

print("\nHighest Run Scorer:", maximum)
print("Runs:", batsmen[maximum])

# Display names only
print("\nNames of Batsmen")

for name in batsmen:
    print(name)

# Add a new batsman
name = input("\nEnter new batsman name: ")
runs = int(input("Enter runs: "))

batsmen[name] = runs

print("\nDictionary after adding player")

print(batsmen)

# Remove batsman with lowest runs
lowest = min(batsmen, key=batsmen.get)

del batsmen[lowest]

print("\nDictionary after removing lowest scorer")

print(batsmen)