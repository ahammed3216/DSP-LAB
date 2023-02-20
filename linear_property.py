
import numpy as np

x=np.random.rand(1,10)
y=np.random.rand(1,10)

sum=x+y
result1=np.fft.fft(sum.flatten())

dft1=np.fft.fft(x.flatten())
dft2=np.fft.fft(y.flatten())

result2=dft1+dft2

print('LHS',result1)
print('RHS',result2)

print("CHECK",result2-result1)

