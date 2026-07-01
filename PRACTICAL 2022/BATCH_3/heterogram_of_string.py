s=input("Enter the string:")
result=s.replace(" ","")
# print(result)

# u1=set(result)
# if len(result)==len(u1):
#     print("This string is heterogram")
# else:
#     print("NOT")


#method 2
flag=0
for ch in range(len(result)):
    if result[ch] in result[ch+1:]:
        flag=1
        break
if flag==1:
    print("Not heterogram")
else:
    print("Heterogram")