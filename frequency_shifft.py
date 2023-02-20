import numpy as np

# Cicular frequency shift
x = [2, 3, 4, 5, 6]
N = len(x)
k = np.arange(N)

X = np.abs(np.fft.fft(x))
print(X)

l = 2
x_shifted = x * np.exp(1j * 2 * np.pi * k * l / N)

print(np.abs(np.fft.fft(x_shifted)))