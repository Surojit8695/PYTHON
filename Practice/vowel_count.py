file = "C:\\Users\\suroj\\OneDrive\\Desktop\\PYTHON\\Practice\\source.txt"
connt = 0  # Note: You have a typo here (connt), but it is not used in the loops anyway
fp = open(file, "r")
lines = fp.readlines()#read file line by line in one single list
fp.close()

with open("destination.txt", "w") as out:
    for line in lines:
        count = 0  # Resets the vowel count for the new line

        # 1. Loop through each character in the line directly
        for ch in line.lower():  # Added .lower() so it counts capital A, E, I, O, U too!
            if ch in "aeiou":
                count += 1

        # 2. FIXED INDENTATION: Move this out of the character loop!
        # This now runs exactly ONCE per line after counting all vowels.
        out.write(line.rstrip() + " Vowels=" + str(count) + "\n")
