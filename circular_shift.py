import numpy as np

# Cicular time shift
x = [2, 3, 4, 5, 6]
k = np.arange(len(x))

l = 2
X = np.fft.fft(x)
x_shifted_freq = X * np.exp(-1j * 2 * np.pi * k * l / len(x))

x_shifted = np.fft.ifft(x_shifted_freq)
print(np.abs(x_shifted))