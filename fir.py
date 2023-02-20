import numpy as np 
import matplotlib.pyplot as plt 
from scipy import signal
from math import pi 
N=25;
Q=np.floor(N/2);
n=np.arange(-Q,Q+1,1)
h=np.zeros(N)
vc=0.1
for idx in np.arange(N):
 if n[idx]==0:
    h[idx]=vc 
else:
 h[idx]=np.sin(vc*pi*n[idx])/(pi*n[idx])
win=np.kaiser(N,1);
h=h*win;

w,H=signal.freqz(b=h,a=1)
y=20*np.log10(abs(h))
print(len(w))
plt.plot(w/pi)
plt.show()
