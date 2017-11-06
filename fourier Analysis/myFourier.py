##Manual fourier analysis.

#Import necessary libraries. (do not use numpy.fft)
import numpy as np
#from scipy.io import wavfile
import matplotlib.pyplot as plt
pi=np.pi

#create sample data with frequency of 2pi
nums=np.arange(0,10*pi,pi/50)
data=np.sin(nums)

#show the sample data
plt.plot(nums,data)

waveIntensity=[]
soundArray=[]
waveRange=np.arange(0,4*pi,pi/50)

for curWave in waveRange:
    soundArray=data#[:int(50*curWave/pi)] #only use 1 wavelength
    #what distance is wavelength?
    tempIntensity=sum([tData-np.sin(curWave*t)-np.cos(curWave*t) for tData,t in zip(soundArray,nums)])
    waveIntensity.append(tempIntensity)
    print tempIntensity

plt.plot(waveIntensity)
plt.show()

##for frequency in freqRange:
##    tempIntensity=0
##    print sum([np.sin(tData)+np.cos(tData) for tData in data])
##    for tData in data:
##        #for each data point find sin+cos of that point
##        #put this data into an list
##        tempIntensity+=np.sin(tData)+np.cos(tData)
##    freq.append(tempIntensity)
##    print tempIntensity

#display fourier

#remake function

#compare to original
