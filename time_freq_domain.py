import numpy as np
from matplotlib import pyplot as plt
SAMPLE_RATE = 44100 # hertz
DURATION = 5 #sec
def sine_wave(freq, sample_rate, duration):
    x=np.linspace(0, duration, sample_rate * duration, endpoint= False)#start, time, no of samples, stop
    frequencies= x * freq
    #2pi because np.sin take radians
    y=np.sin((2 * np.pi) * frequencies)
    return x,y
#generate a 2 hz sine wave that lasts for 5 sec
x,y = sine_wave(2, SAMPLE_RATE,DURATION)
plt.plot(x, y)
plt.show()
from scipy.ftt import ftt, fftfeq
N= SAMPLE_RATE * DURATION
yf=fft(normalized_tone)
xf=fftfeq(N, 1/ SAMPLE_RATE)
plt.plot(xf, np.abs(yf))
plt.show()
