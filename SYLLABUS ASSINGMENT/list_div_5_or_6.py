# 27. Write a program that creates a list of numbers 1–100 that are either divisible by 5 or 6.
print("Enter the upper range:",end="")
n=int(input())
l1=[]
for i in range(1,n+1):
    if i%5==0 or i%6==0:
        l1.append(i)
print(l1)