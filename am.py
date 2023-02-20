import numpy as np
import matplotlib.pyplot as plt
fc = 100
fm = 5
fs = 6400
Vc = 10
Vm = 4
time_dur  = 0.5
N = time_dur * fs
ts = 1/fs
n = np.arange(0,N,1)
t = n * ts
x = (Vc + Vm * np.cos(2 * np.pi * fm * t)) * np.cos(2 * np.pi * fc * t) 
plt.plot(x)
plt.show()