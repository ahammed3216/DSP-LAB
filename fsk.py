import matplotlib.pyplot as plt
import numpy as np
from math import pi
import numpy as np
import matplotlib.pyplot as plt
from math import pi

fc1=100
fc2=400

fs=6400   
time_dur=0.01
N=time_dur*fs
n=np.arange(0,N)
ts=1/fs
t=n*ts

x1=np.sin(2*3.14*fc1/fs*n)
x2=np.sin(2*3.14*fc2/fs*n)

plt.subplot(221)
plt.plot(x1)

plt.subplot(222)
plt.plot(x2)

input=[1,0,1,0,0,0]

output=np.array([])
for i in input:
    if i==1:
        output=np.append(output,10*x1)
    else:
        output=np.append(output,x1)

plt.subplot(223)
plt.plot(output)
plt.show()