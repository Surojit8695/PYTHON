# -------------------------------------------------------------
# Question 8
# Write a Python program that defines a class Length.
#
# Include:
# (a) Constructor
# (b) SetLength()
# (c) getLength()
# (d) __str__()
# (e) __add__()
# -------------------------------------------------------------

class Length:

    # Constructor
    def __init__(self, feet=0, inches=0):
        self.feet = feet
        self.inches = inches

    # Set values
    def setLength(self, feet, inches):
        self.feet = feet
        self.inches = inches

    # Return tuple
    def getLength(self):
        return (self.feet, self.inches)

    # Print object
    def __str__(self):
        return f"{self.feet} feet {self.inches} inches"

    # Add two objects
    def __add__(self, other):

        total_inches = self.inches + other.inches
        total_feet = self.feet + other.feet

        if total_inches >= 12:
            total_feet += total_inches // 12
            total_inches = total_inches % 12

        return Length(total_feet, total_inches)


# Driver Program

L1 = Length()

feet = int(input("Enter feet for first length: "))
inches = int(input("Enter inches for first length: "))

L1.setLength(feet, inches)

L2 = Length()

feet = int(input("Enter feet for second length: "))
inches = int(input("Enter inches for second length: "))

L2.setLength(feet, inches)

print("\nFirst Length :", L1)
print("Second Length:", L2)

L3 = L1 + L2

print("Total Length :", L3)