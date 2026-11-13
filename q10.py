import numpy as np
from scipy.cluster.vq import kmeans2, whiten
customers = np.array([[20, 200], [22, 220], [60, 900], [65, 950]], dtype=float)
scaled = whiten(customers)
centers, labels = kmeans2(scaled, 2, minit="++", seed=42)
print("Cluster labels:", labels)