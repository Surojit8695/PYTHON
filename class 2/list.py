lst1=[1,2,3,4,5,6]
#method 1
print(lst1)
for i in lst1:
    print(i)

#method 2
for i in range(len(lst1)):
    print(lst1[i])

fruit=["apple","Banana","Mango","Pineapple"]
print(fruit)
fruit.append("cucamber")
fruit.append("hello")
print(fruit)
"""
print("Enter the value of x:",end="")
x=int(input())
print("The value of x is:",x)
print("Type of x is:",type(x))


#this is comment
print("This is escape sequence\nAnd a new line")
a=1
b="Surojit"
c=True
d=1.2
e=None
print("Type of a is:",type(a))
print("Type of b is:",type(b))
print("Type of c is:",type(c))
print("Type of d is:",type(d))
print("Type of e is:",type(e))
"""
str1=input("Enter the string:")
print(str1)
print(str1[0:3])
print(len(str1))
print(str1.upper())
print(str1.lower())
print(str1.rstrip("!"))#it will remove the all the ! present at the end
print(str1.split())

str2="welcoMe to The CITy of joy"
print(str2.capitalize())

str3="Welcome to the page.ik this is enough"
print(str3.center(50))

str4="surojit saha hello world surojit kolkata surojit"
print(str4.count("surojit"))
