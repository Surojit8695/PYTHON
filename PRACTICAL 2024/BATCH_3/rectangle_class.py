# 5. Write a Python class namely Rectangle. It must have two members - length and width. Keep method
# calculateArea() that will compute the area of a rectangle.
# Keep necessary validations.
# Both input values will be read from a text file.

class Rectangle:
    
    def __init__(self):
        self.length=0
        self.width=0

    def readData(self, filename):
        fp = open(filename, "r")
        self.length = int(fp.readline())
        self.width = int(fp.readline())
        fp.close()

    def calculateArea(self):
        area=self.length*self.width
        return area
    
r1=Rectangle()
r1.readData("C:\\Users\\suroj\\OneDrive\\Desktop\\PYTHON\\PRACTICAL 2024\\BATCH_3\\rectangle.txt")
print(r1.calculateArea())

##Pass values as parameters to the method
# r1 = Rectangle()
# print(r1.calculateArea(10, 20))

##Read input inside the method
# class Rectangle:
#     def calculateArea(self):
#         length = int(input("Enter length: "))
#         width = int(input("Enter width: "))

#         return length * width

# r1 = Rectangle()
# print(r1.calculateArea())


##create a separate setter method
# class Rectangle:

#     def setData(self, length, width):
#         self.length = length
#         self.width = width

#     def calculateArea(self):
#         return self.length * self.width

# r1 = Rectangle()
# r1.setData(10, 20)
# print(r1.calculateArea())


##read data through file
# def readData(self, filename):
#         fp = open(filename, "r")
#         self.length = int(fp.readline())
#         self.width = int(fp.readline())
#         fp.close()