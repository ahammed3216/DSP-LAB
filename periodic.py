import matplotlib.pyplot as plt
import numpy as np

x=[1,2,3,3,5]
N=len(x)
n=2
k=2
print(x[n])
print(x[N-n])
X=np.fft.fft(x)
print(abs(X[k]))
print(abs(X[N-k]))