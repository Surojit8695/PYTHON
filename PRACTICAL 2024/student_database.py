flag=1
count=1
student={}
while 1:
    print(f"Enter the details for student:{count}")
    name=input("Enter the student name:")
    dob=input("Enter the student dob:")
    year=input("Enter the year of admission:")
    dept=input("Enter the department namer:")
    student[name]={"dob":dob,"year":year,"dept":dept}
    count+=1
    flag=int(input("Do you want to add more student details(1=Yes/2=No):"))
    
    if flag==0:
        break

print(student)

file1="C:\\Users\\suroj\\OneDrive\\Desktop\\PYTHON\\2024Practical\\students.txt"
fp=open(file1,"w")
for key ,value in student.items():
    fp.write(f"Name:{key}\n")
    fp.write(f"Date of birth:{value["dob"]}\n")
    fp.write(f"Year of admission:{value["year"]}\n")
    fp.write(f"Department name:{value["dept"]}\n")
    fp.write("------------------------------------------")
    # fp.write("-" * 30 + "\n")
fp.close()
print("Student details added successfully")