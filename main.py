# import tests.test_descriptive_statistics
# import tests.test_hypothesis_testing


import numpy as np
import src.hypothesis_testing as ht
import src.distributions as dist

distribution = np.random.normal(
    loc = 46,
    scale = 3.1,
    size = 1000
)

print(ht.kolmogorov_smirnov_test(
    empirical_distribution = distribution,
    theoritical_distribution = lambda x: dist.normal_distribution(
        x = x,
        mean = 46,
        standard_deviation = 3.1
    )
))