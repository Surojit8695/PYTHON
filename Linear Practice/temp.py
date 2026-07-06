# Question 11
# Draw suitable diagrams to represent both absolute and
# cumulative frequencies for the given family size data.
#
# Hint:
# Use plt.bar() for absolute frequency and
# plt.plot(np.cumsum(frequency)) for cumulative frequency.
#family_size = [2, 3, 4, 5, 6, 7, 8, 9, 10]
#frequency = [26, 21, 17, 12, 9, 3, 2, 2, 1]

import numpy as np
import matplotlib.pyplot as plt

family_size=np.array([2, 3, 4, 5, 6, 7, 8, 9, 10])
frequency =np.array([26, 21, 17, 12, 9, 3, 2, 2, 1])
plt.figure(figsize=(8,4))
plt.bar(family_size,frequency,color='green')
plt.ylabel("Frequency")
plt.xlabel("Family_size")
plt.title("Absoutoute Frequency")
plt.grid(axis='y')
# plt.ylim(20,100)
# plt.xticks(family_size)
plt.savefig("graph.png")#Save Figure automatically
plt.show()

# cum_sum=np.cumsum(frequency)
# print(cum_sum)

# plt.plot(family_size,cum_sum,marker='o',linestyle='--',color='red',
#          linewidth=2,
#          markersize=8)
# plt.ylabel("Cum_Frequency")
# plt.xlabel("Family_size")
# plt.title("Cumulative Frequency")
# plt.grid(True)
# plt.show()

# plt.scatter([70,60,30],[10,20,30])
# plt.show()

# data=[10,20,30,40,50]

# plt.boxplot(data)
# plt.show()

# x=[1,2,3,4]
# y=[2,5,4,6]

# # plt.stem(x,y)
# # plt.show()

# plt.plot(x,y,label="Sales")

# plt.show()

