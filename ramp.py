import numpy as np
import matplotlib.pyplot as plt


def ramp(t):
    return t*np.array(t>0)

t=np.linspace(-2,2,1000)
plt.plot(t,ramp(t))
plt.show()