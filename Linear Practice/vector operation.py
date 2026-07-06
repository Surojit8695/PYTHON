import numpy as np
import matplotlib.pyplot as plt
data = np.random.randint(1,100,50)

plt.hist(data,
         bins=10,
         edgecolor='black')
plt.show()