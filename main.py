import src.descriptive_statistics as ds
import src.distributions as dist
import scipy.stats as stat
import numpy as np
import matplotlib.pyplot as plt


X = np.linspace(-5, 5, 1000)
Y = [ dist.uniform_distribution(x, 1, 3) for x in X ]

plt.plot(X, Y)
plt.show()
