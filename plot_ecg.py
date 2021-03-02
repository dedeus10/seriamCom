import numpy as np
import matplotlib.pyplot as plt

ecg = np.loadtxt('ecg_data.txt')
print(len(ecg))
plt.plot(ecg[1000:])
plt.show()