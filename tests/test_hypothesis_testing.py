from math import sqrt
from scipy.stats import norm, ttest_1samp, ttest_ind, ttest_rel

from src.descriptive_statistics import mean, standard_deviation
from src.hypothesis_testing import (
    one_sample_t_test, independent_samples_t_test, dependent_samples_t_test,
    one_sample_z_test, independent_samples_z_test, dependent_samples_z_test
)


def print_comparison(label, custom, scipy):
    print(f"\n{label} (t-test)")
    print(f"Your result:     t = {custom['t-statictics']:.5f}, p = {custom['p-value']:.5f}")
    print(f"SciPy result:    t = {scipy.statistic:.5f}, p = {scipy.pvalue:.5f}")
    print(f"Difference:      Δt = {abs(custom['t-statictics'] - scipy.statistic):.5f}, Δp = {abs(custom['p-value'] - scipy.pvalue):.5f}")


def print_z_comparison(label, custom, expected_z, expected_p):
    print(f"\n{label} (z-test, manual check)")
    print(f"Your result:     z = {custom['z-statictics']:.5f}, p = {custom['p-value']:.5f}")
    print(f"Manual result:   z = {expected_z:.5f}, p = {expected_p:.5f}")
    print(f"Difference:      Δz = {abs(custom['z-statictics'] - expected_z):.5f}, Δp = {abs(custom['p-value'] - expected_p):.5f}")


# -----------------------
# Test data
# -----------------------
sample = [2.1, 2.5, 1.8, 2.9, 2.2]
population_mean = 2.0
population_std = 0.3

sample1 = [1.9, 2.5, 3.1, 2.8]
sample2 = [2.2, 2.7, 3.3, 3.0]
pop_std_1 = 0.25
pop_std_2 = 0.3

before = [10, 12, 9, 11, 13]
after = [11, 11, 10, 13, 14]
differences = [a - b for a, b in zip(after, before)]
differences_std = standard_deviation(differences)


# -----------------------
# T-TESTS
# -----------------------

# One-sample t-test
custom_result = one_sample_t_test(sample, population_mean)
scipy_result = ttest_1samp(sample, population_mean)
print_comparison("One-sample t-test", custom_result, scipy_result)

# Independent samples t-test (Welch)
custom_result = independent_samples_t_test(sample1, sample2)
scipy_result = ttest_ind(sample1, sample2, equal_var=False)
print_comparison("Independent samples t-test", custom_result, scipy_result)

# Dependent samples (paired) t-test
custom_result = dependent_samples_t_test(differences)
scipy_result = ttest_rel(before, after)
print_comparison("Dependent samples t-test", custom_result, scipy_result)


# -----------------------
# Z-TESTS (manual validation)
# -----------------------

# One-sample z-test
custom_result = one_sample_z_test(sample, population_mean, population_std)
expected_z = (mean(sample) - population_mean) / (population_std / sqrt(len(sample)))
expected_p = 2 * (1 - norm.cdf(abs(expected_z)))
print_z_comparison("One-sample z-test", custom_result, expected_z, expected_p)

# Independent samples z-test
custom_result = independent_samples_z_test(sample1, sample2, pop_std_1, pop_std_2)
expected_z = (mean(sample1) - mean(sample2)) / sqrt(
    (pop_std_1 ** 2 / len(sample1)) + (pop_std_2 ** 2 / len(sample2))
)
expected_p = 2 * (1 - norm.cdf(abs(expected_z)))
print_z_comparison("Independent samples z-test", custom_result, expected_z, expected_p)

# Dependent samples z-test
custom_result = dependent_samples_z_test(differences, differences_std)
expected_z = mean(differences) / (differences_std / sqrt(len(differences)))
expected_p = 2 * (1 - norm.cdf(abs(expected_z)))
print_z_comparison("Dependent samples z-test", custom_result, expected_z, expected_p)
