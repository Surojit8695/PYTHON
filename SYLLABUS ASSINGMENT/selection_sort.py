# 25. Write a program to sort the elements in ascending order using selection sort.L
def selection_sort(a):
    n=len(a)
    for i in range(n-1):
        min=i
        for j in range(i+1,n):
            if a[j]<a[min]:
                min=j
        a[i],a[min]=a[min],a[i]
    return a

n=int(input("Enter the number of element:"))
l1=[]
for i in range(n):
    val=int(input("Enter the val:"))
    l1.append(val)

print("Original list is:",l1)
print("List after sort:",selection_sort(l1))
