import numpy as np
import matplotlib.pyplot as plt

def half_wave_rectifier(signal):
    rectified_signal = np.zeros(len(signal))
    for i in range(len(signal)):
        if signal[i] >= 0:
            rectified_signal[i] = signal[i]
        else:
            rectified_signal[i] = np.abs(signal[i])
    return rectified_signal

# Generate a sinusoidal signal
time = np.linspace(0, 1, 1000)
signal = np.sin(2 * np.pi * 10 * time)
plt.subplot(121)
plt.plot(signal)
# Rectify the signal
rectified_signal = half_wave_rectifier(signal)

# Plot the original and rectified signals
plt.subplot(122)
plt.plot(time, rectified_signal, label='Rectified Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.legend()
plt.show()