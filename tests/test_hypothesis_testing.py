from scipy.stats import ttest_1samp, ttest_ind, ttest_rel
from src.descriptive_statistics import mean, variance, standard_deviation
from src.distributions import cummulative_distribution_function, t_student_distribution
from src.univariate_calculus import absolute_value
from src.hypothesis_testing import one_sample_t_test, independent_samples_t_test, dependent_samples_t_test

def print_comparison(label, custom, scipy):
    print(f"\n{label}")
    print(f"Your result:     t = {custom['t-statictics']:.5f}, p = {custom['p-value']:.5f}")
    print(f"SciPy result:    t = {scipy.statistic:.5f}, p = {scipy.pvalue:.5f}")
    print(f"Difference:      Δt = {abs(custom['t-statictics'] - scipy.statistic):.5f}, Δp = {abs(custom['p-value'] - scipy.pvalue):.5f}")

# Example test data
sample = [2.1, 2.5, 1.8, 2.9, 2.2]
population_mean = 2.0

sample1 = [1.9, 2.5, 3.1, 2.8]
sample2 = [2.2, 2.7, 3.3, 3.0]

before = [10, 12, 9, 11, 13]
after  = [11, 11, 10, 13, 14]
differences = [a - b for a, b in zip(after, before)]

# One-sample t-test
custom_result = one_sample_t_test(sample, population_mean)
scipy_result = ttest_1samp(sample, population_mean)
print_comparison("One-sample t-test", custom_result, scipy_result)

# Independent samples t-test (Welch’s by default in scipy)
custom_result = independent_samples_t_test(sample1, sample2)
scipy_result = ttest_ind(sample1, sample2, equal_var=False)
print_comparison("Independent samples t-test", custom_result, scipy_result)

# Dependent samples (paired) t-test
custom_result = dependent_samples_t_test(differences)
scipy_result = ttest_rel(before, after)
print_comparison("Dependent samples t-test", custom_result, scipy_result)
