import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

f1=100
f2=1000
fs=6400
ts=1/fs
time_dur=0.01
N=time_dur*fs
n=np.arange(0,N,1)
x1=np.sin(2*np.pi*f1/fs*n)
x2=np.sin(2*np.pi*f2/fs*n)
rslt=x1+x2

plt.subplot(221)
plt.plot(x1)

plt.subplot(222)
plt.plot(x2)

plt.subplot(223)
plt.plot(rslt)

spect=np.fft.fft(rslt)

plt.subplot(224)
plt.plot(np.abs(spect))
plt.show()


fc=1000
fn=fs/2
vc=2*fc/fs
h=np.zeros(25)
Q=np.floor(25/2)
a=np.arange(-Q,Q+1,1)
print(a)
for idx in np.arange(25):
    if a[idx]==0:
        h[idx]=vc
    else:
        h[idx]=np.sin(vc*np.pi*a[idx]/(np.pi*a[idx]))
win=np.kaiser(25,1)
h=h*win

w,h=signal.freqz(b=h,a=1)
y=10*np.log10(abs(h))
plt.plot(w/3.14,y)
plt.show()
