from src.descriptive_statistics import mean, variance, standard_deviation
from src.distributions import continuous_cummulative_distribution_function, discrete_cummulative_distribution_function, t_student_distribution, normal_distribution
from src.univariate_calculus import absolute_value
from src.constants import e


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


def one_sample_t_test(sample: list[float], population_mean: float) -> dict:
    length = len(sample)
    degrees_of_freedom = length - 1
    t = one_sample_t_statistic(
        sample = sample,
        population_mean = population_mean
    )
    response = {
        't-statictics': t,
        'p-value': 2 * ( 1 - continuous_cummulative_distribution_function( 
            distribution = lambda x: t_student_distribution(
                x = x,
                degrees_of_freedom = degrees_of_freedom
            ),
            x = absolute_value(t)
        ) ),
        'degrees_of_freedom': degrees_of_freedom
    }
    return response


def independent_samples_t_test(sample_one: list[float], sample_two: list[float]) -> dict:
    length_one = len(sample_one)
    length_two = len(sample_two)
    degrees_of_freedom = ( length_one + length_two ) - 2
    t = independent_samples_t_statistics(
        sample_one = sample_one,
        sample_two = sample_two
    )
    response = {
        't-statictics': t,
        'p-value': 2 * ( 1 - continuous_cummulative_distribution_function( 
            distribution = lambda x: t_student_distribution(
                x = x,
                degrees_of_freedom = degrees_of_freedom
            ),
            x = absolute_value(t)
        ) ),
        'degrees_of_freedom': degrees_of_freedom
    }
    return response


def dependent_samples_t_test(differences: list[float]) -> dict:
    length = len(differences)
    degrees_of_freedom = length - 1
    t = dependent_samples_t_statistic(
        differences = differences
    )
    response = {
        't-statictics': t,
        'p-value': 2 * ( 1 - continuous_cummulative_distribution_function( 
            distribution = lambda x: t_student_distribution(
                x = x,
                degrees_of_freedom = degrees_of_freedom
            ),
            x = absolute_value(t)
        ) ),
        'degrees_of_freedom': degrees_of_freedom
    }
    return response


def one_sample_z_statistic(sample: list[float], population_mean: float, population_standard_deviation: float = None) -> float:
    if population_standard_deviation is None:
        return one_sample_t_statistic(
            sample = sample,
            population_mean = population_mean
        )
    else:
        length = len(sample)
        return ( mean(data = sample) - population_mean ) / ( population_standard_deviation / ( length ** 0.5 ) )


def independent_samples_z_statistics(sample_one: list[float], sample_two: list[float], population_standard_deviation_one: float = None, population_standard_deviation_two: float = None) -> float:
    if population_standard_deviation_one is None or population_standard_deviation_two is None:
        return independent_samples_t_statistics(
            sample_one = sample_one,
            sample_two = sample_two
        )
    else:
        length_one = len(sample_one)
        length_two = len(sample_two)
        return ( mean(sample_one) - mean(sample_two) ) / \
            ( ( ( population_standard_deviation_one ** 2 ) \
                / length_one + ( population_standard_deviation_two ** 2 ) / length_two ) ** 0.5 )


def dependent_samples_z_statistic(differences: list[float], differences_standard_deviation: float = None) -> float:
    if differences_standard_deviation is None:
        return dependent_samples_t_statistic(
            differences = differences
        )
    else:
        length = len(differences)
        return ( mean(data = differences) - 0 ) / ( differences_standard_deviation / ( length ** 0.5 ) )


def one_sample_z_test(sample: list[float], population_mean: float, population_standard_deviation: float = None) -> dict:
    length = len(sample)
    degrees_of_freedom = length
    if population_standard_deviation is None:
        degrees_of_freedom = degrees_of_freedom - 1
    z = one_sample_z_statistic(
        sample = sample,
        population_mean = population_mean,
        population_standard_deviation = population_standard_deviation
    )
    response = {
        'z-statictics': z,
        'p-value': 2 * ( 1 - continuous_cummulative_distribution_function( 
            distribution = lambda x: normal_distribution(
                x = x,
                mean = 0,
                standard_deviation = 1
            ),
            x = absolute_value(z)
        ) ),
        'degrees_of_freedom': degrees_of_freedom
    }
    return response


def independent_samples_z_test(sample_one: list[float], sample_two: list[float], population_standard_deviation_one: float = None, population_standard_deviation_two: float = None) -> dict:
    length_one = len(sample_one)
    length_two = len(sample_two)
    degrees_of_freedom = ( length_one + length_two )
    if population_standard_deviation_one is None and population_standard_deviation_two is None:
        degrees_of_freedom = degrees_of_freedom - 2
    z = independent_samples_z_statistics(
        sample_one = sample_one,
        sample_two = sample_two,
        population_standard_deviation_one = population_standard_deviation_one,
        population_standard_deviation_two = population_standard_deviation_two
    )
    response = {
        'z-statictics': z,
        'p-value': 2 * ( 1 - continuous_cummulative_distribution_function( 
            distribution = lambda x: normal_distribution(
                x = x,
                mean = 0,
                standard_deviation = 1
            ),
            x = absolute_value(z)
        ) ),
        'degrees_of_freedom': degrees_of_freedom
    }
    return response


def dependent_samples_z_test(differences: list[float], differences_standard_deviation: float = None) -> dict:
    length = len(differences)
    degrees_of_freedom = length
    if differences_standard_deviation is None:
        degrees_of_freedom = degrees_of_freedom - 1
    z = dependent_samples_z_statistic(
        differences = differences,
        differences_standard_deviation = differences_standard_deviation
    )
    response = {
        'z-statictics': z,
        'p-value': 2 * ( 1 - continuous_cummulative_distribution_function( 
            distribution = lambda x: normal_distribution(
                x = x,
                mean = 0,
                standard_deviation = 1
            ),
            x = absolute_value(z)
        ) ),
        'degrees_of_freedom': degrees_of_freedom
    }
    return response


def d_statistics(sample: list[float], distribution):
    differences = []
    for datum in sample:
        differences.append(absolute_value(
            x = discrete_cummulative_distribution_function(
                distribution = sample,
                x = datum
            ) - continuous_cummulative_distribution_function(
                distribution = distribution,
                x = datum
            )
        ))
    maximum_difference = differences[0]
    for difference in differences:
        if difference > maximum_difference:
            maximum_difference = difference
    return maximum_difference


def kolmogorov_function(parameter_lambda: float, end: int = 100):
    counter = 0
    for i in range(1, end + 1):
        counter = counter + ( ( ( -1 ) ** ( i - 1)) * e( -2 * ( i ** 2 ) * ( parameter_lambda ** 2 ) ) )
    return 2 * counter


def kolmogorov_smirnov_test(empirical_distribution: list[float], theoritical_distribution: list[float]):
    length = len(empirical_distribution)
    d = d_statistics(
        sample = empirical_distribution,
        distribution = theoritical_distribution
    )
    response = {
        'd-statistics': d,
        'p-value': kolmogorov_function(
            parameter_lambda = d * ( length ** 0.5 )
        )
    }
    return response