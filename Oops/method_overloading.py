#  Method overloading means having multiple methods with the same name but different numbers or types of parameters.
# Does Python Support Method Overloading?

# No. Python does not support traditional method overloading like Java or C++
class Demo:

    def add(self, a):
        print(a)

    def add(self, a, b):
        print(a + b)


d = Demo()

d.add(10, 20)
d2=Demo()
# d2.add(10) #will through an error
# The first add() method is overwritten by the second one.


# How to Achieve Method Overloading in Python

# Python provides alternative ways to handle different numbers of arguments.

# Method 1: Using Default Arguments (Most Common)
# -------------------------------------------------------------
# Method Overloading using Default Arguments
# -------------------------------------------------------------

class Calculator:

    def add(self, a, b=0):
        print("Sum =", a + b)


c = Calculator()

c.add(10)
c.add(10, 20)


# -------------------------------------------------------------
# Method Overloading using *args
# -------------------------------------------------------------

class Calculator:

    def add(self, *numbers):
        print("Sum =", sum(numbers))


c = Calculator()

c.add(10)
c.add(10, 20)
c.add(10, 20, 30)
c.add(10, 20, 30, 40)