from cmath import exp, pi
import numpy
 
def fft(x):
    N = len(x)
    if N <= 1: return x
    even = fft(x[0::2])
    odd =  fft(x[1::2])
    return [even[k] + exp(-2j*pi*k/N)*odd[k] for k in xrange(N/2)] + \
           [even[k] - exp(-2j*pi*k/N)*odd[k] for k in xrange(N/2)]

import random
data=[float(20*random.random()) for i in range(20)]
print data
print( ' '.join("%5.3f" % abs(f) for f in fft(data) ))
