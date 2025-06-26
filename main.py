import src.descriptive_statistics as ds
import src.distributions as dist
import src.hypothesis_testing as ht
import src.univariate_calculus as ucalc
import scipy.stats as stat
import numpy as np
import matplotlib.pyplot as plt


f = lambda x: 4 * x ** 2

print(ucalc.integral_rectangles_method(f, 0, 3))
print(ucalc.integral_trapezoidal_method(f, 0, 3))
print(ucalc.integral_simpsons_method(f, 0, 3))