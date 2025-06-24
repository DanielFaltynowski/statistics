import src.descriptive_statistics as ds
import src.distributions as dist
import src.hypothesis_testing as ht
import scipy.stats as stat
import numpy as np
import matplotlib.pyplot as plt


p_values = [0.71, 0.81, 0.91, 0.01, 0.11, 0.21, 0.31, 0.41, 0.51, 0.61]
print(ht.benjamini_hockberg_method(p_values))