import numpy as np
from scipy.signal import find_peaks
vibration = np.array([1, 2, 1, 3, 2, 8, 2, 1, 7, 2, 1])
peaks, properties = find_peaks(vibration, height=5)
print("Peak positions:", peaks) 
print("Peak values:", vibration[peaks]) 