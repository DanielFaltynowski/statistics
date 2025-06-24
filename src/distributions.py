from src.constants import pi, e


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
        print('Invalid input: `uniform_distribution(x, a, b)`')
        return None
    return ( 1 / ( ( 2 * pi() * ( standard_deviation ** 2 ) ) ** 0.5 ) ) * \
          ( e() ** ( -1 * ( ( (x - mean) ** 2 ) / ( 2 * ( standard_deviation ** 2 ) ) ) ) )


def exponential_distribution(x: float, parameter_lambda: float) -> float:
    if not isinstance(x, (int, float)) or not isinstance(parameter_lambda, (int, float)):
        print('Invalid input: `uniform_distribution(x, a, b)`')
        return None
    if x < 0:
        return 0
    else:
        return parameter_lambda * ( e() ** ( -1 * parameter_lambda * x ) )