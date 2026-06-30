n=int(input("Enter the number of range:"))
count=0
for i in range(1,n+1):
    if(n%i==0):
        count=count+1
if count==2:
    print(n,"is a prime number")
else:
    print(n,"is a not prime number")
