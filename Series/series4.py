n=int(input("Enter the number of range:"))
sum=0
for i in range(1,n+1):
    if i%2==0:
        sum=sum+i
        #print(i,end=" ")
print("Sum is:",sum)