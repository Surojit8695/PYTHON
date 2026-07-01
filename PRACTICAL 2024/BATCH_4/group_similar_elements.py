test_list=[4,6,6,4,2,2,4,8,5,8]
result={}
for i in test_list:
    if i not in result:
        result[i]=[i]
    else:
        result[i].append(i)
print(result)