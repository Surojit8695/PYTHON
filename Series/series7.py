n=int(input("Enter the number of range:"))
a=0
b=1
print(a)
print(b)
for i in range(3,n+1):
    sum=a+b
    print(sum)
    a=b
    b=sum
