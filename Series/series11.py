n=int(input("Enter the number of range:"))
sum=0
for i in range(1,n+1):
    sum=sum+(i*i/i)
print("Sum is:",round(sum,2))