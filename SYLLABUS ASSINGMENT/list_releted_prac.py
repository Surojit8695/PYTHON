n=int(input("Enter the number of element(N):"))
l1=[]
for i in range(n):
    l1.append(int(input("Enter the val:")))

print(l1)
odd_list=[]
even_list=[]

for j in l1:
    if j%2!=0:
        odd_list.append(j)
    else:
        even_list.append(j)
print("Even list:",even_list)
print("Odd list:",odd_list)