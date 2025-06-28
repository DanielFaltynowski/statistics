import src.descriptive_statistics as ds

import numpy as np
import random
import scipy
import scipy.stats
import statsmodels.stats.weightstats




distribution = np.random.chisquare(
    df = 5,
    size = 1000
)

weights = [ random.randint(100, 150) for i in range(len(distribution)) ]

print('MEAN')
print('My Library:       ', ds.mean(distribution))
print('Python Library:   ', np.mean(distribution), '\n')

print('MEDIAN')
print('My Library:       ', ds.median(distribution))
print('Python Library:   ', np.median(distribution), '\n')

print('MODE')
print('My Library:       ', ds.mode(distribution))
print('Python Library:   ', scipy.stats.mode(distribution), '\n')

print('POPULATION VARIANCE')
print('My Library:       ', ds.variance(distribution, from_sample = False))
print('Python Library:   ', np.var(distribution, ddof = 0), '\n')

print('SAMPLE VARIANCE')
print('My Library:       ', ds.variance(distribution))
print('Python Library:   ', np.var(distribution, ddof = 1), '\n')

print('POPULATION STANDARD DEVIATION')
print('My Library:       ', ds.standard_deviation(distribution, from_sample = False))
print('Python Library:   ', np.std(distribution, ddof = 0), '\n')

print('SAMPLE STANDARD DEVIATION')
print('My Library:       ', ds.standard_deviation(distribution))
print('Python Library:   ', np.std(distribution, ddof = 1), '\n')

print('POPULATION SKEWNESS')
print('My Library:       ', ds.skewness(distribution, from_sample = False))
print('Python Library:   ', scipy.stats.skew(distribution, bias = True), '\n')

print('SAMPLE SKEWNESS')
print('My Library:       ', ds.skewness(distribution))
print('Python Library:   ', scipy.stats.skew(distribution, bias = False), '\n')

print('POPULATION KURTOSIS')
print('My Library:       ', ds.kurtosis(distribution, from_sample = False))
print('Python Library:   ', scipy.stats.kurtosis(distribution, bias = True) + 3, '\n')

print('SAMPLE KURTOSIS')
print('My Library:       ', ds.kurtosis(distribution))
print('Python Library:   ', scipy.stats.kurtosis(distribution, bias = False) + 3, '\n')

print('POPULATION EXCESS KURTOSIS')
print('My Library:       ', ds.excess_kurtosis(distribution, from_sample = False))
print('Python Library:   ', scipy.stats.kurtosis(distribution, bias = True), '\n')

print('SAMPLE EXCESS KURTOSIS')
print('My Library:       ', ds.excess_kurtosis(distribution))
print('Python Library:   ', scipy.stats.kurtosis(distribution, bias = False), '\n')

print('WEIGHTED MEAN')
print('My Library:       ', ds.weighted_mean(distribution, weights))
print('Python Library:   ', np.average(distribution, weights=weights), '\n')

print('WEIGHTED POPULATION VARIANCE')
print('My Library:       ', ds.weighted_variance(distribution, weights, from_sample=False))
print('Python Library:   ', 'Not available in standard Python libraries\n')

print('WEIGHTED SAMPLE VARIANCE')
print('My Library:       ', ds.weighted_variance(distribution, weights, from_sample=True))
print('Python Library:   ',
      statsmodels.stats.weightstats.DescrStatsW(distribution, weights=weights).var, '\n')

print('WEIGHTED POPULATION STANDARD DEVIATION')
print('My Library:       ', ds.weighted_standard_deviation(distribution, weights, from_sample=False))
print('Python Library:   ', 'Not available in standard Python libraries\n')

print('WEIGHTED SAMPLE STANDARD DEVIATION')
print('My Library:       ', ds.weighted_standard_deviation(distribution, weights, from_sample=True))
print('Python Library:   ',
      statsmodels.stats.weightstats.DescrStatsW(distribution, weights=weights).std, '\n')

print('WEIGHTED POPULATION SKEWNESS')
print('My Library:       ', ds.weighted_skewness(distribution, weights, from_sample=False))
print('Python Library:   ', 'Not available in standard Python libraries\n')

print('WEIGHTED SAMPLE SKEWNESS')
print('My Library:       ', ds.weighted_skewness(distribution, weights))
print('Python Library:   ', 'Not available in standard Python libraries\n')

print('WEIGHTED POPULATION KURTOSIS')
print('My Library:       ', ds.weighted_kurtosis(distribution, weights, from_sample=False))
print('Python Library:   ', 'Not available in standard Python libraries\n')

print('WEIGHTED SAMPLE KURTOSIS')
print('My Library:       ', ds.weighted_kurtosis(distribution, weights))
print('Python Library:   ', 'Not available in standard Python libraries\n')

print('WEIGHTED POPULATION EXCESS KURTOSIS')
print('My Library:       ', ds.weighted_excess_kurtosis(distribution, weights, from_sample=False))
print('Python Library:   ', 'Not available in standard Python libraries\n')

print('WEIGHTED SAMPLE EXCESS KURTOSIS')
print('My Library:       ', ds.weighted_excess_kurtosis(distribution, weights))
print('Python Library:   ', 'Not available in standard Python libraries\n')
