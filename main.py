import src.descriptive_statistics as ds
import scipy.stats as stat
import numpy as np


data_1 = [ 12, 14, 14, 17, 18 ]
data_2 = [ 15, 15, 15, 15, 15 ]

print(ds.moment(data_1, order=1))
print(ds.moment(data_1, order=2))
print(ds.moment(data_1, order=3))
print(ds.moment(data_1, order=4))
print()
print(ds.centralised_moment(data_1, order=2))
print(ds.centralised_moment(data_1, order=3))
print(ds.centralised_moment(data_1, order=4))
print()
print(ds.standardised_moment(data_1, order=3))
print(ds.standardised_moment(data_1, order=4))
print()
print(ds.moment(data_1, order=1), '=', ds.mean(data_1), '=', np.mean(data_1))
print(ds.centralised_moment(data_1, order=2), '=', ds.variance(data_1, from_sample=False), '=', np.var(data_1, ddof=0))
print(ds.standardised_moment(data_1, order=3), '=', ds.skewness(data_1, from_sample=False), '=', stat.skew(data_1))
print(ds.standardised_moment(data_1, order=4), '=', ds.kurtosis(data_1, from_sample=False), '=', stat.kurtosis(data_1, fisher=False))
print()
print(ds.median([3, 1, 2, 4]))
print(ds.mode([1, 2, '3']))
print(ds.data_range([11.5, 2, 1, 7, 3.9, 2.3, 10.3, 6.9]))