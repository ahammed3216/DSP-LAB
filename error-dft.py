import numpy as np
import matplotlib.pyplot as plt
from math import pi

row_index=np.array([np.arange(4)])
col_index=row_index.T
index_mtx=col_index@row_index
exp_mtx=np.exp((-1j*2*pi*index_mtx)/4)
input_mtx=np.random.rand(4,1)
dft_mtx=exp_mtx@input_mtx
fft_mtx=np.fft.fft(input_mtx.flatten())

print(dft_mtx)
print(fft_mtx)
err_mtx=np.abs(dft_mtx.flatten() - fft_mtx )
plt.ylim([-0.5,0.5])

plt.stem(err_mtx)
plt.show()