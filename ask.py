import numpy as np
import matplotlib.pyplot as plt

fc=10
fs = 640
ts = 1 / fs
time_dur = 0.5
N = time_dur * fs
n = np.arange(N)
t = n * ts
y = np.sin(2 * np.pi * fc * n)
plt.plot(t, y)

x = [1, 0, 0, 1, 0, 1, 0]
op = np.array([])
for i in x:
  if i == 1:
    op = np.append(op, 10 * y)
  else:
    op = np.append(op, 5 * y)

plt.figure()
plt.plot(op)
plt.show()