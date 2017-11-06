print 'importing libaries'
import pyaudio
import struct
import matplotlib.pyplot as plt
import time

FORMAT = pyaudio.paFloat32
SAMPLEFREQ = 44100 #Audio Rate (number of measurements per second)
FRAMESIZE = 1024 #How many data points you grab from the audio stream in a chunk
NSeconds=5 #How many seconds you record for
NOFFRAMES = int(SAMPLEFREQ/FRAMESIZE*NSeconds)
p = pyaudio.PyAudio()
print('running')

data=[]

stream = p.open(format=FORMAT,channels=1,rate=SAMPLEFREQ,input=True,frames_per_buffer=FRAMESIZE)
fig=plt.figure()
plt.ion()
#plt.ylim(-1,1)

startTime=time.time()

for i in range(0,NOFFRAMES):#all the problems with time taken happen in the loop
    tempdata=stream.read(FRAMESIZE)
    newStart=int((time.time()-startTime)*44100)#could be better?
    decoded=struct.unpack(str(FRAMESIZE)+'f',tempdata)#Better way?
    plt.plot(xrange(newStart,newStart+FRAMESIZE),decoded)#Different function? Diffrent range?
    plt.xlim(max(newStart-12000,0),newStart+FRAMESIZE)#Could we fix the max?
    plt.draw()

print time.time()-startTime

stream.stop_stream()
stream.close()
p.terminate()
print('done')
plt.close()
