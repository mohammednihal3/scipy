import numpy as np
from scipy.fft import fft, fftfreq
sample_rate = 1000
time = np.arange(1000) / sample_rate
signal_data = np.sin(2 * np.pi * 50 * time)
frequencies = fftfreq(len(signal_data), 1 / sample_rate)
spectrum = np.abs(fft(signal_data))
positive = frequencies > 0
peak = frequencies[positive][np.argmax(spectrum[positive])]
print("Dominant frequency:", peak, "Hz")