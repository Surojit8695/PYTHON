# -------------------------------------------------------------
# File Name : exception_handling_demo.py
# -------------------------------------------------------------
# Python Program to Demonstrate Exception Handling
#
# Concepts Covered:
# 1. try block
# 2. except block
# 3. Multiple except blocks
# 4. else block
# 5. finally block
# 6. Exception as e
# 7. raise keyword
# 8. User-defined Exception
# 9. FileNotFoundError
# 10. IndexError
# 11. KeyError
# -------------------------------------------------------------


# -------------------------------------------------------------
# User-defined Exception
# -------------------------------------------------------------
class InvalidAgeError(Exception):
    pass


print("========== Exception Handling Demo ==========\n")


# -------------------------------------------------------------
# Example 1 : try, except, else and finally
# -------------------------------------------------------------
print("Example 1 : Division Program")

try:
    num1 = int(input("Enter first number : "))
    num2 = int(input("Enter second number : "))

    result = num1 / num2

except ValueError:
    print("Error : Please enter integers only.")

except ZeroDivisionError:
    print("Error : Division by zero is not allowed.")

else:
    print("Result =", result)

finally:
    print("Example 1 Completed.\n")


# -------------------------------------------------------------
# Example 2 : IndexError
# -------------------------------------------------------------
print("Example 2 : List Index")

numbers = [10, 20, 30]

try:
    index = int(input("Enter list index : "))
    print("Element =", numbers[index])

except IndexError:
    print("Error : Index out of range.")

except ValueError:
    print("Error : Invalid index.")

finally:
    print("Example 2 Completed.\n")


# -------------------------------------------------------------
# Example 3 : KeyError
# -------------------------------------------------------------
print("Example 3 : Dictionary Key")

student = {
    "name": "Rahul",
    "age": 20
}

try:
    key = input("Enter dictionary key : ")
    print(student[key])

except KeyError:
    print("Error : Key does not exist.")

finally:
    print("Example 3 Completed.\n")


# -------------------------------------------------------------
# Example 4 : File Handling Exception
# -------------------------------------------------------------
print("Example 4 : File Handling")

try:
    file = open("sample.txt", "r")
    print(file.read())
    file.close()

except FileNotFoundError:
    print("Error : File not found.")

finally:
    print("Example 4 Completed.\n")


# -------------------------------------------------------------
# Example 5 : Exception Object (Exception as e)
# -------------------------------------------------------------
print("Example 5 : Exception Object")

try:
    value = int(input("Enter an integer : "))
    print("100 / value =", 100 / value)

except Exception as e:
    print("Exception occurred :", e)

finally:
    print("Example 5 Completed.\n")


# -------------------------------------------------------------
# Example 6 : raise Keyword
# -------------------------------------------------------------
print("Example 6 : raise Keyword")

try:
    marks = int(input("Enter marks : "))

    if marks < 0 or marks > 100:
        raise ValueError("Marks should be between 0 and 100.")

    print("Marks =", marks)

except ValueError as e:
    print("Error :", e)

finally:
    print("Example 6 Completed.\n")


# -------------------------------------------------------------
# Example 7 : User-defined Exception
# -------------------------------------------------------------
print("Example 7 : User-defined Exception")

try:
    age = int(input("Enter age : "))

    if age < 18:
        raise InvalidAgeError("Age must be 18 or above.")

    print("Eligible for voting.")

except InvalidAgeError as e:
    print("Custom Exception :", e)

except ValueError:
    print("Please enter a valid age.")

finally:
    print("Example 7 Completed.\n")


# -------------------------------------------------------------
# Example 8 : Multiple Exceptions in One except
# -------------------------------------------------------------
print("Example 8 : Multiple Exceptions")

try:
    a = int(input("Enter numerator : "))
    b = int(input("Enter denominator : "))

    print("Answer =", a / b)

except (ValueError, ZeroDivisionError):
    print("Either invalid input or division by zero occurred.")

finally:
    print("Example 8 Completed.\n")


# -------------------------------------------------------------
# Program End
# -------------------------------------------------------------
print("========== Program Finished Successfully ==========")