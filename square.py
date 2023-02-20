import numpy as np
import matplotlib.pyplot as plt
from math import pi

def square(t,T,D):
    frac,int_part=np.modf(t%T)
    return(2*(frac<T*D)-1)

t=np.linspace(-2,2,1000)
plt.plot(t,square(t,0.5,0.5))
plt.show()