import numpy as np
import matplotlib.pyplot as plt

def bipolar(t,T,D):
    frac,int_part=np.modf(t%T)
    print(frac)
    return (2*(frac<T*D) -1)

t=np.linspace(-2,2,1000)
plt.plot(t,bipolar(t,1,0.5))
plt.show()