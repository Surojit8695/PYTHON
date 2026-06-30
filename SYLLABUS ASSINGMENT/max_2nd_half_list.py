# 26. Write a program that prints the maximum value of the second half of the list.
l1=[10,15,12,11,8,17,2]
mid=len(l1)//2
print(mid)
l2=l1[mid:]
max=l2[0]
for i in range(len(l2)):
    if l2[i]>max:
        max=l2[i]
print("The maximum element of thr 2nd half of the list is:",max)