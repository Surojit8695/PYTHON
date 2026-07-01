# -------------------------------------------------------------
# Question 3(b)
# Write a program to create a function "show_employee"
# that accepts employee name and salary and displays both.
# -------------------------------------------------------------

# Function definition
def show_employee(name, salary):

    print("Employee Name :", name)

    print("Employee Salary :", salary)


# Driver Program
emp_name = input("Enter employee name: ")

emp_salary = float(input("Enter employee salary: "))

show_employee(emp_name, emp_salary)