import numpy as np
import matplotlib.pyplot as plt
from math import pi

fc=100
fs=10000
time_dur=0.1
N=fs*time_dur
n=np.arange(1,N,1)
data=2*np.sin(2*pi*fc/fs*n)

plt.plot(data)
plt.show()