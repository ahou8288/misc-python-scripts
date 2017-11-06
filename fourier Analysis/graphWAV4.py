import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt



def show_info(aname, a):
    print "Array", aname
    print "shape:", a.shape
    print "dtype:", a.dtype
    print "min, max:", a.min(), a.max()

rate, data = wavfile.read('triangle.wav')
jumpsize=len(data)
plt.plot(data)

show_info("data", data)
for i in range(1):
    top=jumpsize*i+jumpsize
    base=jumpsize*i
    fourierData=np.fft.fft(data[base:top])
    #print fourierData
    plt.figure(i)
    plt.plot(data[base:top])
    plt.plot(fourierData)
plt.show()
