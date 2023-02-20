import numpy as np
import matplotlib.pyplot as plt

# Define the number of bits
N = 1000

# Generate random binary data
data = np.random.randint(0, 2, N)

# Define the carrier frequency
fc = 1000

# Define the sampling frequency
fs = 10000

# Define the time vector
t = np.arange(0, N/fs, 1/fs)

# Generate the carrier signal
carrier = np.cos(2 * np.pi * fc * t)

# Generate the BPSK modulated signal
bpsk = 2 * data - 1
modulated_signal = carrier * bpsk

# Plot the BPSK modulated signal
plt.plot(t, modulated_signal)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('BPSK Modulated Signal')
plt.grid(True)
plt.show()