import pyaudio
import struct
import matplotlib.pyplot as plt

FORMAT = pyaudio.paFloat32
SAMPLEFREQ = 44100
FRAMESIZE = 1024
NSeconds=5
NOFFRAMES = int(SAMPLEFREQ/FRAMESIZE*NSeconds
p = pyaudio.PyAudio()
print('running')

data=[]

stream = p.open(format=FORMAT,channels=1,rate=SAMPLEFREQ,input=True,frames_per_buffer=FRAMESIZE)
fig=plt.figure()
plt.ion()
plt.ylim(-1,1)

for i in range(0,NOFFRAMES):
    tempdata=stream.read(FRAMESIZE)
    decoded=struct.unpack(str(FRAMESIZE)+'f',tempdata)
    plt.plot(xrange(FRAMESIZE*i,i*FRAMESIZE+FRAMESIZE),decoded)
    plt.xlim(max(FRAMESIZE*(i-2),0),FRAMESIZE*i+FRAMESIZE)
    plt.draw()

stream.stop_stream()
stream.close()
p.terminate()
print('done')
plt.close()

