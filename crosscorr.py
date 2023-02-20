import numpy as np

# First signal 
sig1 = np.sin(np.r_[-1:1:0.1])

# Seconds signal with pi/4 phase shift. Half the size of sig1
sig2 = np.sin(np.r_[-1:0:0.1] + np.pi/4)

''' Python only implementation '''

# Pre-allocate correlation array
corr = (len(sig1) - len(sig2) + 1) * [0]

# Go through lag components one-by-one
for l in range(len(corr)):
    corr[l] = sum([sig1[i+l] * sig2[i] for i in range(len(sig2))])

print(corr)