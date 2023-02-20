import numpy as np
import matplotlib.pyplot as plt

fc = 5000
fs = 640000
time_dur = 0.001

ts = 1/fs
N = time_dur*fs
n = np.arange(0, N, 1)
t = n * ts
chirp = np.sin(2 * np.pi * (5 * 10**6 * t + 5000) * t)
plt.plot(chirp)
chirp_fft = np.fft.fft(chirp)
plt.figure()
plt.show()