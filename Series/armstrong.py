n=int(input("Enter the number of range:"))
temp=n
dig=len(str(n))
sum=0
#print(dig)
while temp>0:
    rem=temp%10
    sum=sum+(rem**dig)
    temp=temp//10
if sum==n:
    print("This is a armstring number")
else:
    print("This is not armstrong number")

