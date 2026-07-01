# num="569338"
# # for i in num:
# #     print(num.count(str(i)))

# print(num.count("32"))
s=input("Enter the number:")
d={}
for i in range(10):
    d[i]=s.count(str(i))
    #print(str(i))
print(d)