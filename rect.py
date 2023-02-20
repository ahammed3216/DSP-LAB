import numpy as np
import matplotlib.pyplot as plt

def rect(t,PW):
    return( 1*np.array(np.abs(t)<.0 1))

plt.subplot(2,2,1)
t=np.linspace(-2,2,1000)
plt.plot(t,rect(t,2))
plt.show()