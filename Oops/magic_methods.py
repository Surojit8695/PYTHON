class MagicMethod:

    # Constructor
    def __init__(self, x):
        self.x = x

    # Normal Method
    def display(self):
        print("Value:", self.x)

    # String Representation
    def __str__(self):
        return "Value: " + str(self.x)

    # len()
    def __len__(self):
        return 5

    # +
    def __add__(self, other):
        return self.x + other.x

    # Destructor
    def __del__(self):
        print("Destructor Called")


m1 = MagicMethod("Surojit Saha")

print(m1.x)

m1.display()

print(len(m1))

print(m1)

s = MagicMethod("Rahul")

print(s)

n1 = MagicMethod(10)
n2 = MagicMethod(20)

print("Addition =", n1 + n2)