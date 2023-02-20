import matplotlib.pyplot as plt
import numpy as np

Fs=10000
fc=100
t_dur=.01
N=t_dur*Fs
n=np.arange(N)
sine=1+np.sin(2*3.14*fc/Fs*n)
plt.subplot(221)
plt.plot(sine)

def pcm_encode(signal, bit_depth):
    max_value = 2**bit_depth - 1
    quantized_signal = np.clip(np.round(signal * max_value), 0, max_value).astype(np.int32)
    print(quantized_signal)
    return quantized_signal
plt.subplot(222)
plt.plot(pcm_encode(sine,5))

plt.show()