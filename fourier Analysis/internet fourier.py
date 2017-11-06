from cmath import exp, pi
import numpy as np
import matplotlib.pyplot as plt

 
def fft(x):
    N = len(x)
    if N <= 1: return x
    even = fft(x[0::2])
    odd =  fft(x[1::2])
    if len(even)<>len(odd): print'what'
    return [even[k] + exp(-2j*pi*k/N)*odd[k] for k in xrange(N/2)] + [even[k] - exp(-2j*pi*k/N)*odd[k] for k in xrange(N/2)]

nums=np.arange(0,10*pi,pi/50)
data=np.sin(nums)

plt.plot(fft(data))
plt.show()
