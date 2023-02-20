import numpy as np

# Time reversal
x = [1, 2, 3, 4, 4, 3, 2]
N = len(x)
n = 2
x_fft = np.fft.fft(x)
print(x_fft)
print('x[N - n] :', x[::-1])
x_fft = np.fft.fft(x[::-1])
print('X[N - k] :', np.abs(np.fft.ifft(x_fft)))