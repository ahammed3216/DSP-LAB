import matplotlib.pyplot as plt
import numpy as np


Fs = 8000
f = 5
sample = 64
x = np.arange(sample)
y = np.sin(2 * np.pi * f * x / Fs)
print(y)
plt.plot(x, y)
plt.xlabel('sample(n)')
plt.ylabel('voltage(V)')
plt.show()