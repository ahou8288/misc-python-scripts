print 'Importing libraies.'
import Queue #used to send data
import threading #used to run both at once
import time #used to record when events happen
import pyaudio #used to get data
import struct #used to decoded raw data from pyaudio so that it can be graphed
import matplotlib.pyplot as plt

print 'Libaries Imported.'

plt.ion() #Allow graph to be updated
plt.ylim(-1,1) #all data falls in this range

class AudioThread(threading.Thread):
    def __init__(self):
        super(AudioThread, self).__init__() #what does this do?
        self.p=pyaudio.PyAudio()
        self.stream=self.p.open(format=pyaudio.paFloat32,channels=1,rate=44100,input=True,frames_per_buffer=1024) #use this to get the audio
        self.qAudio=Queue.Queue() #use this to store data once recorded

    def run(self):
        #get audio
        startTime=time.time()
        while time.time()-startTime<5: #run only for 5 seconds
            self.qAudio.put(self.stream.read(1024)) #constantly record data in chunks of 1024
            #this gets data in blocks of duration (1024/44100) seconds.

class PlotThread(threading.Thread):
    def __init__(self,audioSource):
        super(PlotThread, self).__init__()
        self.fig=plt.figure()
        self.lastXval=0
        self.audioSource=audioSource #use this reference to the other class to access the queue where data is stored

    def run(self):
        startTime2=time.time()
        while time.time()-startTime2<5 or self.audioSource.qAudio.not_empty: #run for 5 seconds and also finish plotting the data
            if self.audioSource.qAudio.not_empty:
                print 'Plotting data'
                #Collect the audio data from the queue
                soundData=self.audioSource.qAudio.get()
                #convert the data into a usable/plotable format
                decoded=struct.unpack(str(1024)+'f',soundData)
                #plot this
                self.lastXval+=len(decoded) #this stops the graph being plotted ontop of itself.
                plt.plot(range(self.lastXval,self.lastXval+1024), decoded) #add data to graph
                plt.draw() #draw graph
            else:
                print 'No data to plot.'

print 'Initialising threads.'
thread1=AudioThread()
thread2=PlotThread(thread1)
thread1.start()
thread2.start()
print 'Threads started.'
thread1.join()
thread2.join()
print 'Program finished.'
