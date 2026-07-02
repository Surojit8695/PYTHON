# Program 4
# Given a list of elements, group similar elements
# as different key-value lists in a dictionary.
test_list=[4,6,6,4,2,2,4,8,5,8]
result={}
for i in test_list:
    if i not in result:
        result[i]=[i]
    else:
        result[i].append(i)
print(result)

# output:{4: [4, 4, 4], 6: [6, 6], 2: [2, 2], 8: [8, 8], 5: [5]}