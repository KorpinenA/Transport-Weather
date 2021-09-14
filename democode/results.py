import numpy as np
import matplotlib.pyplot as plt

probability_n = np.array([3830622, 147269, 99882, 74693, 58560, 41226, 31137, 37908, 65163, 60643, 42886])
bins = np.array([0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])

plt.title('Freezing probabilities')
plt.subplot(2, 1, 1)
plt.plot(bins, probability_n)
plt.ylabel('Number of measurements')

plt.subplot(2, 1, 2)
plt.plot(bins[1:], probability_n[1:])
plt.xlabel('Probability')
plt.show()