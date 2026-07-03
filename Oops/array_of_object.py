class Students:
    def input(self):
        self.name=input("Enter the name:")
        self.roll=int(input("Enter the roll:"))
        self.marks=int(input("Enter the marks:"))
    def display(self):
        print("Name:",self.name)
        print("Roll:",self.roll)
        print("Marks:",self.marks)

n=int(input("Enter the number of student details(N):"))
obj=[]

for i in range(n):
    s=Students()
    s.input()
    obj.append(s)
print("Records of the students are:")
count=1
for s in obj:
    print(f"Students {count}")
    s.display()
    count+=1


