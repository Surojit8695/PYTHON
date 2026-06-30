fruits=["Apple","Banana","Cherry"]
print(fruits)

bollist=[True ,False,True,True,False]
print(bollist)

numlist = [1, 5, 7, 9, 3]
print(numlist)

multilist=["Apple",56,True,10.2,"Banana"]
print(multilist)

print(type(multilist))#the type of the datatype

thislist = list(("apple", "banana", "cherry"))
print(thislist)

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1]) #[len(thislist)-4:len(thislist)-1]


thislist = ["apple", "banana", "cherry"]
ap=thislist[0]
if ap in thislist:
  print("Yes, 'apple' is in the fruits list")

  thislist3 = ["apple", "banana", "cherry"]
thislist3[1:3] = ["watermelon"]
print(thislist3)
