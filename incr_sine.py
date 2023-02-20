import matplotlib.pyplot as plt
import numpy as np
fc=800
fs=6400
time_dur=0.01
N=time_dur*fs
n=np.arange(0,N,1)
Ts=1/fs

x=n*np.sin(2*3.14*fc/fs*n)

plt.plot(x)
plt.show()