# -------------------------------------------------------------
# File Name : inheritance_demo.py
# -------------------------------------------------------------
# Python Program to Demonstrate Inheritance
#
# Concepts Covered:
# 1. Single Inheritance
# 2. Multilevel Inheritance
# 3. Multiple Inheritance
# 4. Hierarchical Inheritance
# 5. Hybrid Inheritance
# 6. Constructor Inheritance
# 7. Method Overriding
# 8. super() Function
# 9. isinstance() Function
# 10. issubclass() Function
# -------------------------------------------------------------


# =============================================================
# Base Class
# =============================================================

class Person:

    def __init__(self, name):
        self.name = name
        print("Person Constructor Called")

    def display(self):
        print("Name :", self.name)


# =============================================================
# SINGLE INHERITANCE
# =============================================================

class Student(Person):

    def __init__(self, name, roll):
        super().__init__(name)          # Calling Parent Constructor
        self.roll = roll

    def show(self):
        print("Roll :", self.roll)


print("\n========== SINGLE INHERITANCE ==========")

s = Student("Rahul", 101)
s.display()
s.show()


# =============================================================
# MULTILEVEL INHERITANCE
# =============================================================

class College(Student):

    def __init__(self, name, roll, college):
        super().__init__(name, roll)
        self.college = college

    def details(self):
        print("College :", self.college)


print("\n========== MULTILEVEL INHERITANCE ==========")

c = College("Amit", 102, "ABC College")
c.display()
c.show()
c.details()


# =============================================================
# MULTIPLE INHERITANCE
# =============================================================

class Sports:

    def sports(self):
        print("Plays Cricket")


class Music:

    def music(self):
        print("Loves Music")


class AllRounder(Sports, Music):

    def intro(self):
        print("I am an All Rounder Student")


print("\n========== MULTIPLE INHERITANCE ==========")

a = AllRounder()

a.intro()
a.sports()
a.music()


# =============================================================
# HIERARCHICAL INHERITANCE
# =============================================================

class Animal:

    def sound(self):
        print("Animals make sound")


class Dog(Animal):

    def bark(self):
        print("Dog Barks")


class Cat(Animal):

    def meow(self):
        print("Cat Meows")


print("\n========== HIERARCHICAL INHERITANCE ==========")

d = Dog()
d.sound()
d.bark()

print()

cat = Cat()
cat.sound()
cat.meow()


# =============================================================
# HYBRID INHERITANCE
# (Combination of Hierarchical + Multiple)
# =============================================================

class Father:

    def father_property(self):
        print("Father's Property")


class Mother:

    def mother_property(self):
        print("Mother's Property")


class Child(Father, Mother):

    def own_property(self):
        print("Child's Property")


print("\n========== HYBRID INHERITANCE ==========")

child = Child()

child.father_property()
child.mother_property()
child.own_property()


# =============================================================
# METHOD OVERRIDING
# =============================================================

class Vehicle:

    def start(self):
        print("Vehicle Starts")


class Car(Vehicle):

    # Overriding Parent Method
    def start(self):
        print("Car Starts with Push Button")


print("\n========== METHOD OVERRIDING ==========")

car = Car()
car.start()


# =============================================================
# super() FUNCTION
# =============================================================

class Employee:

    def __init__(self):
        print("Employee Constructor")

    def work(self):
        print("Employee Works")


class Manager(Employee):

    def __init__(self):

        # Calling Parent Constructor
        super().__init__()

        print("Manager Constructor")

    def work(self):

        # Calling Parent Method
        super().work()

        print("Manager Manages Team")


print("\n========== super() FUNCTION ==========")

m = Manager()
m.work()


# =============================================================
# isinstance() FUNCTION
# =============================================================

print("\n========== isinstance() ==========")

print(isinstance(s, Student))
print(isinstance(s, Person))
print(isinstance(s, College))


# =============================================================
# issubclass() FUNCTION
# =============================================================

print("\n========== issubclass() ==========")

print(issubclass(Student, Person))
print(issubclass(College, Student))
print(issubclass(Dog, Animal))


# =============================================================
# Method Resolution Order (MRO)
# =============================================================

print("\n========== METHOD RESOLUTION ORDER ==========")

print(AllRounder.__mro__)


# =============================================================
# Program End
# =============================================================

print("\n========== Program Completed ==========")