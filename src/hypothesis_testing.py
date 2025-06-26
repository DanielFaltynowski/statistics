from src.descriptive_statistics import mean, variance, standard_deviation
from src.distributions import cummulative_distribution_function, t_student_distribution
from src.univariate_calculus import absolute_value


def benjamini_hockberg_method(p_values: list[float]) -> list[float]:
    for p_value in p_values:
        if not isinstance(p_value, (int, float)) or not 0 <= p_value <= 1:
            print('Invalid Input `benjamini_hockberg_method(p_values)`')
    reduced_p_values = p_values[:]
    reduced_p_values.sort()
    length = len(p_values)
    i = length - 2
    while i >= 0:
        bh = reduced_p_values[i] * ( length / ( i + 1 ) )
        if bh < reduced_p_values[i + 1]:
            reduced_p_values[i] = bh
        else:
            reduced_p_values[i] = reduced_p_values[i + 1]
        i = i - 1
    return reduced_p_values


def one_sample_t_statistic(sample: list[float], population_mean: float) -> float:
    length = len(sample)
    return ( mean(data = sample) - population_mean ) / ( standard_deviation(data = sample) / ( length ** 0.5 ) )


def independent_samples_t_statistics(sample_one: list[float], sample_two: list[float]) -> float:
    length_one = len(sample_one)
    length_two = len(sample_two)
    return ( mean(sample_one) - mean(sample_two) ) / \
           ( ( variance(sample_one) / length_one + variance(sample_two) / length_two ) ** 0.5 )


def dependent_samples_t_statistic(differences: list[float]) -> float:
    length = len(differences)
    return ( mean(data = differences) - 0 ) / ( standard_deviation(data = differences) / ( length ** 0.5 ) )


def one_sample_t_test(sample: list[float], population_mean: float, degrees_of_freedom: int) -> float:
    t = one_sample_t_statistic(
        sample = sample,
        population_mean = population_mean
    )
    response = {
        't-statictics': t,
        'p-value': 2 * ( 1 - cummulative_distribution_function( 
            distribution = lambda x: t_student_distribution(
                x = x,
                degrees_of_freedom = degrees_of_freedom
            ),
            x = absolute_value(t)
        ) )
    }
    return response