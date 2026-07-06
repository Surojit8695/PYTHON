import numpy as np
import matplotlib.pyplot as plt
#family_size=np.array(list(map(int,input("Enter family_size:").split())))
#frequency=np.array(list(map(int,input("Enter frequency:").split())))

family_size = [2, 3, 4, 5, 6, 7, 8, 9, 10]

frequency = [26, 21, 17, 12, 9, 3, 2, 2, 1]
#print("Family Size:",family_size)
#print("Frequency:",frequency)

cum_freq=np.cumsum(frequency)
#print("Cumulative frequency:",cum_freq)

#print("Cumulative frquency table\n")
#print("\nFamily_size\tFrequency\tCum_freq")
#for i in range(len(frequency)):
               #print(family_size[i],"\t\t",frequency[i],"\t\t",cum_freq[i])


plt.figure(figsize=(8,4))
plt.bar(family_size,frequency,color="teal")
plt.grid(True)
plt.xlabel("family_size ---->")
plt.ylabel("frequency ----->")
plt.title("Absouloute Frequency")
plt.show()

plt.plot(family_size,cum_freq,marker="o",color="teal")
plt.xlabel("family_size ---->")
plt.ylabel("cum_frequency ----->")
plt.title("Cumulative Frequency")
plt.grid(True)
plt.show()

#pie chart
mark=[30,40,50,60]
plt.pie(mark,labels=["Math","Physics","Chem","Comp"])
plt.show()
