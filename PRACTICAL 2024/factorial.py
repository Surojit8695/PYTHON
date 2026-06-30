#6. Write a Python program to find factorial of a number both iteratively and recursively.
num=int(input("Enter the number:"))
fact=1
for i in range(1,num+1):
    fact=fact*i


print(fact)
def factorial(n):
    if n==1 or n==0:
        return 1
    else:
        k=n*factorial(n-1)
        return k
    
print(factorial(5))
print(factorial(0))
print(factorial(1))