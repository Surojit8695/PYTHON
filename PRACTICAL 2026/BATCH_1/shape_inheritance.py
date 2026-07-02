# 6. Write a Program in Python to implement a base class Shape
# and derived classes Circle and Rectangle.
#
# (a) The Shape class should have one data member: dim1.
# (b) The Shape class should contain an area() method that displays
#     the message: "Area of Shape:".
# (c) The Rectangle class should have another data member: dim2.
# (d) Override the area() method in each derived class.
# (e) Display the area of each shape.
#
# Area of Circle = 3.14 * dim1 * dim1
# Area of Rectangle = dim1 * dim2


# Base class
class Shape:

    # Constructor
    def __init__(self, dim1):
        self.dim1 = dim1

    # Method to be overridden
    def area(self):
        print("Area of Shape:")


# Derived class Circle
class Circle(Shape):

    # Constructor
    def __init__(self, radius):
        super().__init__(radius)

    # Overriding area() method
    def area(self):
        area = 3.14 * self.dim1 * self.dim1
        print("Area of Circle =", area)


# Derived class Rectangle
class Rectangle(Shape):

    # Constructor
    def __init__(self, length, breadth):
        super().__init__(length)
        self.dim2 = breadth

    # Overriding area() method
    def area(self):
        area = self.dim1 * self.dim2
        print("Area of Rectangle =", area)


# Main Program

# Input for Circle
radius = float(input("Enter the radius of the circle: "))
circle = Circle(radius)

# Input for Rectangle
length = float(input("Enter the length of the rectangle: "))
breadth = float(input("Enter the breadth of the rectangle: "))
rectangle = Rectangle(length, breadth)

print("\nOutput:")
circle.area()
rectangle.area()