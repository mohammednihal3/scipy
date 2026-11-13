import numpy as np
from scipy.ndimage import gaussian_filter

image = np.array([[10, 20, 10],
                  [20, 255, 20],
                  [10, 20, 10]], dtype=float)
smoothed = gaussian_filter(image, sigma=0.7)
print(smoothed)