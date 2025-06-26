import src.descriptive_statistics as ds
import src.distributions as dist
import src.hypothesis_testing as ht
import src.univariate_calculus as ucalc
import scipy.stats as stat
import numpy as np
import matplotlib.pyplot as plt


f = lambda x: x ** 3

X = np.linspace(-5, 5, 1000)
Y = [ dist.t_student_distribution(x, 10 - 1) for x in X ]