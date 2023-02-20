import numpy as np
import matplotlib.pyplot as plt
from math import pi
import time

def gen_exp_matrix(N):
    row_index=np.array([np.arange(N)])
    col_index=row_index.T

    index_matrix=col_index@row_index
    exp_matrix_f=np.exp((-1j*2*pi*index_matrix)/4)
  

    return exp_matrix_f


gamma_values=np.arange(2,13,1)
dft_time=np.zeros(len(gamma_values))
fft_time=np.zeros(len(gamma_values))
idx=0

for gamma in gamma_values:
    M=2**gamma
    input_data=np.random.rand(M,1)

    #DFT TIME CALCULATION
    exp_matrix=gen_exp_matrix(M)
    start_time=time.perf_counter()
    dft_mtx=exp_matrix @ input_data
    end_time=time.perf_counter()

    dft_time[idx]=end_time-start_time

    #FFT TIME CALCULATION
    start_time=time.perf_counter()
    dft_frm_fft_mtx=np.fft.fft(input_data.flatten())
    end_time=time.perf_counter()

    fft_time[idx]=end_time-start_time

    idx=idx+1


plt.plot(gamma_values,dft_time,'r',gamma_values,fft_time,'b')
plt.legend(['DFT MATRIX','FFT MATRIX'])
plt.show()








