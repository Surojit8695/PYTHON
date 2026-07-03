class Person:
    def __init__(self,name):
        self.name=name
    def display(self):
        print("Name is:",self.name)

class Student(Person):
    def __init__(self,name,roll):
        self.roll=roll
        super().__init__(name)
    
    def show(self):
        super().display()
        print("Roll is:", self.roll)

s1=Student("Rahul",101)
# s1.display()
s1.show()

class College(Student):

    def __init__(self, name, roll, college):
        super().__init__(name, roll)
        self.college = college

    def details(self):
        print("College :", self.college)


c = College("Amit", 102, "ABC College")
c.display()
c.show()
c.details()