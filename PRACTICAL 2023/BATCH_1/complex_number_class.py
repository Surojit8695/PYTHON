# -------------------------------------------------------------
# Question:
# Write a Python class to perform addition and multiplication
# of two complex number objects.
# -------------------------------------------------------------

class Complex:

    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def add(self, other):

        return Complex(
            self.real + other.real,
            self.imag + other.imag
        )

    def multiply(self, other):

        real = self.real * other.real - self.imag * other.imag
        imag = self.real * other.imag + self.imag * other.real

        return Complex(real, imag)

    def display(self):
        print(self.real, "+", self.imag, "i")


r1 = int(input("Enter real part of first complex number: "))
i1 = int(input("Enter imaginary part: "))

r2 = int(input("Enter real part of second complex number: "))
i2 = int(input("Enter imaginary part: "))

c1 = Complex(r1, i1)
c2 = Complex(r2, i2)

print("\nAddition:")
c1.add(c2).display()

print("Multiplication:")
c1.multiply(c2).display()