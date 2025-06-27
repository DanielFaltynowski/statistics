import src.hypothesis_testing as ht
import src.constants as const
import src.descriptive_statistics as ds
import src.distributions as dist
import src.univariate_calculus as ucalc

import numpy as np
import random
import scipy
import scipy.stats


# One Sample T-Test (p_value >= 0.05, null hypotghesis confirmed)

population = [ float(value) for value in np.random.normal(
    loc = 17.4,
    scale = 3.2,
    size = 1000
) ]

sample = random.sample(
    population = population,
    k = 15
)

print('One Sample T-Test (p_value >= 0.05, null hypotghesis rejected)')
print('My Library:       ', ht.one_sample_t_test(
    sample = sample,
    population_mean = ds.mean(population)
))
print('Python Library:   ', scipy.stats.ttest_1samp(
    a = sample,
    popmean = ds.mean(population)
), '\n')


# One Sample T-Test (p_value < 0.05, null hypotghesis rejected)

population = [ float(value) for value in np.random.normal(
    loc = 17.4,
    scale = 3.2,
    size = 1000
) ]

sample = [ value + 4 for value in random.sample(
    population = population,
    k = 15
) ]

print('One Sample T-Test (p_value < 0.05, null hypotghesis rejected)')
print('My Library:       ', ht.one_sample_t_test(
    sample = sample,
    population_mean = ds.mean(population)
))
print('Python Library:   ', scipy.stats.ttest_1samp(
    a = sample,
    popmean = ds.mean(population)
), '\n')


# Independent Samples T-Test (p_value >= 0.05, null hypotghesis confirmed)

population = [ float(value) for value in np.random.normal(
    loc = 17.4,
    scale = 3.2,
    size = 1000
) ]

sample_1 = random.sample(
    population = population,
    k = 15
)
sample_2 = random.sample(
    population = population,
    k = 15
)

print('Independent Samples T-Test (p_value >= 0.05, null hypotghesis confirmed)')
print('My Library:       ', ht.independent_samples_t_test(
    sample_one = sample_1,
    sample_two = sample_2
))
print('Python Library:   ', scipy.stats.ttest_ind(
    a = sample_1,
    b = sample_2
), '\n')


# Independent Samples T-Test (p_value < 0.05, null hypotghesis rejected)

population = [ float(value) for value in np.random.normal(
    loc = 17.4,
    scale = 3.2,
    size = 1000
) ]

sample_1 = random.sample(
    population = population,
    k = 15
)
sample_2 = [ value + 4 for value in random.sample(
    population = population,
    k = 15
) ]

print('Independent Samples T-Test (p_value < 0.05, null hypotghesis rejected)')
print('My Library:       ', ht.independent_samples_t_test(
    sample_one = sample_1,
    sample_two = sample_2
))
print('Python Library:   ', scipy.stats.ttest_ind(
    a = sample_1,
    b = sample_2
), '\n')


# Dependent Samples T-Test (p_value >= 0.05, null hypotghesis confirmed)

before = [ float(value) for value in np.random.normal(
    loc = 17.4,
    scale = 3.2,
    size = 15
) ]

after = [ float(value) for value in np.random.normal(
    loc = 17.4,
    scale = 3.2,
    size = 15
) ]

differences = [ after[i] - before[i] for i in range(len(before)) ]

print('Dependent Samples T-Test (p_value >= 0.05, null hypotghesis confirmed)')
print('My Library:       ', ht.dependent_samples_t_test(
    differences = differences
))
print('Python Library:   ', scipy.stats.ttest_rel(
    a = after,
    b = before
), '\n')


# Dependent Samples T-Test (p_value < 0.05, null hypotghesis rejected)

before = [ float(value) for value in np.random.normal(
    loc = 17.4,
    scale = 3.2,
    size = 15
) ]

after = [ float(value) for value in np.random.normal(
    loc = 27.1,
    scale = 3.9,
    size = 15
) ]

differences = [ after[i] - before[i] for i in range(len(before)) ]

print('Dependent Samples T-Test (p_value < 0.05, null hypotghesis rejected)')
print('My Library:       ', ht.dependent_samples_t_test(
    differences = differences
))
print('Python Library:   ', scipy.stats.ttest_rel(
    a = after,
    b = before
), '\n')