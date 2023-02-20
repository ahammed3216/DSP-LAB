###CIRCULAR CONVOLUTION

import numpy as np

N1=5
N2=3

x1=np.random.randint(5,size=N1)
x2=np.random.randint(9,size=N2)


##linear convolution
y=np.convolve(x1,x2)
print(y)
M=max(N1,N2)

##circular convolution
circular_conv=y[0:M]
rem=np.arange(len(y[M:]))
circular_conv[rem]+=y[M:]


print(circular_conv)


