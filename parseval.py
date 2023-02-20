
###PARSEVALS THEOROM
import numpy as np
N=5000

x1=np.random.rand(1,N)+1j*np.random.rand(1,N)
x2=np.random.rand(1,N)+1j*np.random.rand(1,N)

result1=np.sum(x1*x2.conj())

X1=np.fft.fft(x1.flatten())
X2=np.fft.fft(x2.flatten())

result2=(np.sum(X1*X2.conj()))/N

print(result1)
print(result2)