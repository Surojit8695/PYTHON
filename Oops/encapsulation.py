# -------------------------------------------------------------
# File Name : encapsulation_demo.py
# -------------------------------------------------------------
# Python Program to Demonstrate Encapsulation
#
# Concepts Covered:
# 1. Encapsulation
# 2. Public Data Members
# 3. Protected Data Members (_)
# 4. Private Data Members (__)
# 5. Public Methods
# 6. Protected Methods
# 7. Private Methods
# 8. Getter Method
# 9. Setter Method
# 10. Name Mangling
# -------------------------------------------------------------


# =============================================================
# Class Definition
# =============================================================

class Student:

    def __init__(self, name, age, marks):

        # Public Data Member
        self.name = name

        # Protected Data Member
        self._age = age

        # Private Data Member
        self.__marks = marks


    # ---------------------------------------------------------
    # Public Method
    # ---------------------------------------------------------
    def display(self):
        print("Name  :", self.name)
        print("Age   :", self._age)
        print("Marks :", self.__marks)


    # ---------------------------------------------------------
    # Getter Method
    # Used to access private variable
    # ---------------------------------------------------------
    def get_marks(self):
        return self.__marks


    # ---------------------------------------------------------
    # Setter Method
    # Used to modify private variable
    # ---------------------------------------------------------
    def set_marks(self, marks):

        if marks >= 0 and marks <= 100:
            self.__marks = marks
        else:
            print("Invalid Marks")


    # ---------------------------------------------------------
    # Protected Method
    # ---------------------------------------------------------
    def _protected_method(self):
        print("This is a Protected Method.")


    # ---------------------------------------------------------
    # Private Method
    # ---------------------------------------------------------
    def __private_method(self):
        print("This is a Private Method.")


    # Public Method to call Private Method
    def access_private_method(self):
        self.__private_method()



# =============================================================
# Driver Program
# =============================================================

student = Student("Rahul", 20, 85)


print("========== PUBLIC MEMBER ==========")

print(student.name)

student.display()


print("\n========== PROTECTED MEMBER ==========")

# Possible but discouraged
print(student._age)

student._protected_method()


print("\n========== PRIVATE MEMBER ==========")

# Direct access is NOT allowed
# Uncommenting the next line will give an error
# print(student.__marks)


print("Marks using Getter :", student.get_marks())


print("\n========== SETTER METHOD ==========")

student.set_marks(95)

print("Updated Marks :", student.get_marks())


print("\n========== PRIVATE METHOD ==========")

student.access_private_method()


print("\n========== NAME MANGLING ==========")

# Python internally changes __marks to _Student__marks
print(student._Student__marks)


print("\n========== INVALID SETTER ==========")

student.set_marks(120)


print("\n========== FINAL DETAILS ==========")

student.display()


print("\n========== Program Completed ==========")