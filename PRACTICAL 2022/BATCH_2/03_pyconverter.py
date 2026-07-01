# -------------------------------------------------------------
# Question 3
# Create a class PyConverter.
# Convert between kilometer, meter and centimeter.
# -------------------------------------------------------------

class PyConverter:

    def __init__(self, length, unit):

        self.length = length
        self.unit = unit.lower()

    # Convert input to meters
    def to_meter(self):

        if self.unit == "kilometer":
            return self.length * 1000

        elif self.unit == "meter":
            return self.length

        elif self.unit == "centimeter":
            return self.length / 100

    def kilometer(self):

        return self.to_meter() / 1000

    def meter(self):

        return self.to_meter()

    def centimeter(self):

        return self.to_meter() * 100


length = float(input("Enter length: "))
unit = input("Enter unit (kilometer/meter/centimeter): ")

obj = PyConverter(length, unit)

print("Kilometer :", obj.kilometer())
print("Meter :", obj.meter())
print("Centimeter :", obj.centimeter())