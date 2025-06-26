import src.descriptive_statistics as ds
import src.distributions as dist
import src.hypothesis_testing as ht
import src.univariate_calculus as ucalc
import scipy.stats as stat
import numpy as np
import matplotlib.pyplot as plt
import random
from scipy.stats import ttest_1samp


population = list(np.random.normal(7, 2, 1000))
population = [ float(value) for value in population ]
sample = random.sample(population, k = 10)
sample = [ value + 3 for value in sample ]

print(ht.one_sample_t_test(
        sample = sample,
        population_mean = ds.mean(population),
        degrees_of_freedom = len(sample) - 1
    )
)
print(ttest_1samp(
    a = sample,
    popmean = ds.mean(population)
))
