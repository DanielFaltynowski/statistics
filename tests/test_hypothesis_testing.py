import src.hypothesis_testing as ht
import src.descriptive_statistics as ds

import numpy as np
import random
import scipy
import scipy.stats
import statsmodels.stats.weightstats


# One Sample T-Test (p_value >= 0.05, null hypothesis confirmed)

population = [ float(value) for value in np.random.normal(
    loc = 17.4,
    scale = 3.2,
    size = 1000
) ]

sample = random.sample(
    population = population,
    k = 15
)

print('One Sample T-Test (p_value >= 0.05, null hypothesis rejected)')
print('My Library:       ', ht.one_sample_t_test(
    sample = sample,
    population_mean = ds.mean(population)
))
print('Python Library:   ', scipy.stats.ttest_1samp(
    a = sample,
    popmean = ds.mean(population)
), '\n')


# One Sample T-Test (p_value < 0.05, null hypothesis rejected)

population = [ float(value) for value in np.random.normal(
    loc = 17.4,
    scale = 3.2,
    size = 1000
) ]

sample = [ value + 4 for value in random.sample(
    population = population,
    k = 15
) ]

print('One Sample T-Test (p_value < 0.05, null hypothesis rejected)')
print('My Library:       ', ht.one_sample_t_test(
    sample = sample,
    population_mean = ds.mean(population)
))
print('Python Library:   ', scipy.stats.ttest_1samp(
    a = sample,
    popmean = ds.mean(population)
), '\n')


# Independent Samples T-Test (p_value >= 0.05, null hypothesis confirmed)

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

print('Independent Samples T-Test (p_value >= 0.05, null hypothesis confirmed)')
print('My Library:       ', ht.independent_samples_t_test(
    sample_one = sample_1,
    sample_two = sample_2
))
print('Python Library:   ', scipy.stats.ttest_ind(
    a = sample_1,
    b = sample_2
), '\n')


# Independent Samples T-Test (p_value < 0.05, null hypothesis rejected)

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

print('Independent Samples T-Test (p_value < 0.05, null hypothesis rejected)')
print('My Library:       ', ht.independent_samples_t_test(
    sample_one = sample_1,
    sample_two = sample_2
))
print('Python Library:   ', scipy.stats.ttest_ind(
    a = sample_1,
    b = sample_2
), '\n')


# Dependent Samples T-Test (p_value >= 0.05, null hypothesis confirmed)

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

print('Dependent Samples T-Test (p_value >= 0.05, null hypothesis confirmed)')
print('My Library:       ', ht.dependent_samples_t_test(
    differences = differences
))
print('Python Library:   ', scipy.stats.ttest_rel(
    a = after,
    b = before
), '\n')


# Dependent Samples T-Test (p_value < 0.05, null hypothesis rejected)

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

print('Dependent Samples T-Test (p_value < 0.05, null hypothesis rejected)')
print('My Library:       ', ht.dependent_samples_t_test(
    differences = differences
))
print('Python Library:   ', scipy.stats.ttest_rel(
    a = after,
    b = before
), '\n')

###

# One Sample Z-Test with Unknown Standard Deviation (p_value >= 0.05, null hypothesis confirmed)

population = [ float(value) for value in np.random.normal(
    loc = 17.4,
    scale = 3.2,
    size = 1000
) ]

sample = random.sample(
    population = population,
    k = 100
)

print('One Sample Z-Test with Unknown Standard Deviation (p_value >= 0.05, null hypothesis rejected)')
print('My Library:       ', ht.one_sample_z_test(
    sample = sample,
    population_mean = ds.mean(population)
))
print('Python Library:   ', statsmodels.stats.weightstats.ztest(
    x1 = sample,
    value = ds.mean(population)
), '\n')


# One Sample Z-Test with Unknown Standard Deviation (p_value < 0.05, null hypothesis rejected)

population = [ float(value) for value in np.random.normal(
    loc = 17.4,
    scale = 3.2,
    size = 1000
) ]

sample = [ value + 4 for value in random.sample(
    population = population,
    k = 100
) ]

print('One Sample Z-Test with Unknown Standard Deviation (p_value < 0.05, null hypothesis rejected)')
print('My Library:       ', ht.one_sample_z_test(
    sample = sample,
    population_mean = ds.mean(population)
))
print('Python Library:   ', statsmodels.stats.weightstats.ztest(
    x1 = sample,
    value = ds.mean(population)
), '\n')


# Independent Samples Z-Test with Unknown Standard Deviation (p_value >= 0.05, null hypothesis confirmed)

population = [ float(value) for value in np.random.normal(
    loc = 17.4,
    scale = 3.2,
    size = 1000
) ]

sample_1 = random.sample(
    population = population,
    k = 100
)
sample_2 = random.sample(
    population = population,
    k = 100
)

print('Independent Samples Z-Test with Unknown Standard Deviation (p_value >= 0.05, null hypothesis confirmed)')
print('My Library:       ', ht.independent_samples_z_test(
    sample_one = sample_1,
    sample_two = sample_2
))
print('Python Library:   ', statsmodels.stats.weightstats.ztest(
    x1 = sample_1,
    x2 = sample_2
), '\n')


# Independent Samples Z-Test with Unknown Standard Deviation (p_value < 0.05, null hypothesis rejected)

population = [ float(value) for value in np.random.normal(
    loc = 17.4,
    scale = 3.2,
    size = 1000
) ]

sample_1 = random.sample(
    population = population,
    k = 100
)
sample_2 = [ value + 4 for value in random.sample(
    population = population,
    k = 100
) ]

print('Independent Samples Z-Test with Unknown Standard Deviation (p_value < 0.05, null hypothesis rejected)')
print('My Library:       ', ht.independent_samples_z_test(
    sample_one = sample_1,
    sample_two = sample_2
))
print('Python Library:   ', statsmodels.stats.weightstats.ztest(
    x1 = sample_1,
    x2 = sample_2
), '\n')


# Dependent Samples Z-Test with Unknown Standard Deviation (p_value >= 0.05, null hypothesis confirmed)

before = [ float(value) for value in np.random.normal(
    loc = 17.4,
    scale = 3.2,
    size = 100
) ]

after = [ float(value) for value in np.random.normal(
    loc = 17.4,
    scale = 3.2,
    size = 100
) ]

differences = [ after[i] - before[i] for i in range(len(before)) ]

print('Dependent Samples Z-Test with Unknown Standard Deviation (p_value >= 0.05, null hypothesis confirmed)')
print('My Library:       ', ht.dependent_samples_z_test(
    differences = differences
))
print('Python Library:   ', statsmodels.stats.weightstats.ztest(
    x1 = after,
    x2 = before
), '\n')


# Dependent Samples Z-Test with Unknown Standard Deviation (p_value < 0.05, null hypothesis rejected)

before = [ float(value) for value in np.random.normal(
    loc = 17.4,
    scale = 3.2,
    size = 100
) ]

after = [ float(value) for value in np.random.normal(
    loc = 27.1,
    scale = 3.9,
    size = 100
) ]

differences = [ after[i] - before[i] for i in range(len(before)) ]

print('Dependent Samples Z-Test with Unknown Standard Deviation (p_value < 0.05, null hypothesis rejected)')
print('My Library:       ', ht.dependent_samples_z_test(
    differences = differences
))
print('Python Library:   ', statsmodels.stats.weightstats.ztest(
    x1 = after,
    x2 = before
), '\n')