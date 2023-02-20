import numpy as np
import matplotlib.pyplot as plt

x=np.random.randint(6,size=5)
X=np.fft.fft(x.flatten())

k=np.array(np.linspace(0,4))
exp_term=np.exp(-1j*2*3.14*k/5*2)
print(exp_term)