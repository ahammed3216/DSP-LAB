import matplotlib.pyplot as plt
import numpy as np
from math import pi
N1=5
N2=5
x1=np.random.randint(3,size=N1)
x2=np.random.randint(5,size=N2)
y=np.convolve(x1,x2)
print(y)
m=max(N1,N2)
circ_conv=y[0:m]
rem=np.arange(len(y[m:]))
circ_conv[rem]=circ_conv[rem]+y[m:]
print(circ_conv)
X1 = np.fft.fft(x1)
X2 = np.fft.fft(x2)

print(np.abs(np.fft.ifft(X1 * X2)))