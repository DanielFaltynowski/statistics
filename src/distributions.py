from src.constants import pi, e
from src.univariate_calculus import gamma_function, integral_simpsons_method, newton_symbol


def uniform_distribution(x: float, a: float, b: float):
    if not isinstance(x, (int, float)) or not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        print('Invalid input: `uniform_distribution(x, a, b)`')
        return None
    if a > b:
        print('Invalid input: `uniform_distribution(x, a, b)`')
        return None
    if not a <= x <= b:
        return 0
    else:
        return 1 / ( b - a )


def normal_distribution(x: float, mean: float, standard_deviation: float) -> float:
    if not isinstance(x, (int, float)) or not isinstance(mean, (int, float)) or not isinstance(standard_deviation, (int, float)):
        print('Invalid input: `normal_distribution`')
        return None
    return ( 1 / ( ( 2 * pi() * ( standard_deviation ** 2 ) ) ** 0.5 ) ) * \
          ( e() ** ( -1 * ( ( (x - mean) ** 2 ) / ( 2 * ( standard_deviation ** 2 ) ) ) ) )


def exponential_distribution(x: float, parameter_lambda: float) -> float:
    if not isinstance(x, (int, float)) or not isinstance(parameter_lambda, (int, float)):
        print('Invalid input: `exponential_distribution`')
        return None
    if x < 0:
        return 0
    else:
        return parameter_lambda * ( e() ** ( -1 * parameter_lambda * x ) )


def t_student_distribution(x: float, degrees_of_freedom: int):
    return ( ( gamma_function( (degrees_of_freedom + 1) / 2 ) / \
            ( gamma_function( degrees_of_freedom / 2 ) * ( ( degrees_of_freedom * pi() ) ** 0.5) ) ) ) * \
            ( ( 1 + ( ( x ** 2 ) / degrees_of_freedom ) ) ** ( -1 * ( ( degrees_of_freedom + 1 ) / 2 ) ) )


def discrete_cummulative_distribution_function(distribution: list[float], x: float):
    length = len(distribution)
    denominator = length
    nominator = 0
    for datum in distribution:
        if datum <= x:
            nominator = nominator + 1
    return nominator / denominator


def continuous_cummulative_distribution_function(distribution, x: float, start_point: float = -100, n: int = 1000):
    return integral_simpsons_method(
        f = distribution,
        a = start_point,
        b = x,
        n = n
    )


def binomial_distribution(x: int, all_events: int, positive_probability: float) -> float:
    return newton_symbol(
        n = all_events,
        k = x
    ) * ( positive_probability ** x ) * ( ( 1 - positive_probability ) ** ( all_events - x ) )