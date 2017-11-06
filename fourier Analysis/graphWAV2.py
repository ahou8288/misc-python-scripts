from scipy.io.wavfile import read
import matplotlib.pyplot as plt
import os
os.chdir(r'C:\Users\ahoug_000\Music')
# read audio samples
input_data = read('Star Wars - Duel Of The Fates.wav')
audio = input_data[1]
# plot the first 1024 samples
plt.plot(audio[0:1024])
# label the axes
plt.ylabel("Amplitude")
plt.xlabel("Time")
# set the title  
plt.title("Sample Wav")
# display the plot
plt.show()
