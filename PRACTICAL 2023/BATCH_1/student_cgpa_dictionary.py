# -------------------------------------------------------------
# Question:
# Store full name and CGPA of 10 students in a dictionary.
# (a) Print initials with surname.
# (b) Display student having highest CGPA.
# (c) Display students having CGPA below 3.0.
# -------------------------------------------------------------

students = {}

for i in range(10):

    name = input("Enter student name: ")
    cgpa = float(input("Enter CGPA: "))

    students[name] = cgpa

print("\nInitials with surname:")

for name in students:

    parts = name.split()

    if len(parts) >= 2:
        print(parts[0][0] + ".", parts[-1])

highest = max(students, key=students.get)

print("\nHighest CGPA Student")
print(highest, ":", students[highest])

print("\nStudents with CGPA below 3.0")

flag = False

for name, cgpa in students.items():

    if cgpa < 3.0:
        print(name, cgpa)
        flag = True

if not flag:
    print("None")