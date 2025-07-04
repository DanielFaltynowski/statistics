from src.descriptive_statistics import mean, standard_deviation, variance


def covariance(data_X: list[float], data_Y: list[float], from_sample: bool = True) -> float:
    length = len(data_X)
    denominator = length
    if from_sample:
        denominator = denominator - 1
    data_X_mean = mean(data_X)
    data_Y_mean = mean(data_Y)
    nominator = 0
    for i in range(length):
        nominator = nominator + ( ( data_X[i] - data_X_mean ) * ( data_Y[i] - data_Y_mean ) )
    return nominator / denominator


def correlation(data_X: list[float], data_Y: list[float], from_sample: bool = True) -> float:
    nominamor = covariance(
        data_X = data_X,
        data_Y = data_Y,
        from_sample = from_sample
    )
    denominamor = standard_deviation(
        data = data_X,
        from_sample = from_sample
    ) * standard_deviation(
        data = data_Y,
        from_sample = from_sample
    )
    return nominamor / denominamor


def residual_sum_of_squares(Y_observed: list[float], Y_predicted: list[float]) -> float:
    length = len(Y_observed)
    response = 0
    for i in range(length):
        response = response + ( ( Y_observed - Y_predicted ) ** 2 )
    return response


def mean_square_error(Y_observed: list[float], Y_predicted: list[float]) -> float:
    length = len(Y_observed)
    nominator = residual_sum_of_squares(
        Y_observed = Y_observed,
        Y_predicted = Y_predicted
    )
    denominator = length
    return nominator / denominator


def r_square(Y_observed: list[float], Y_predicted: list[float], from_sample: bool = True) -> float:
    length = len(Y_observed)
    nominator = residual_sum_of_squares(
        Y_observed = Y_observed,
        Y_predicted = Y_predicted
    )
    denominator = length * variance(
        data = Y_observed,
        from_sample = from_sample
    )
    return 1 - ( nominator / denominator )


def linear_regression_params(data_X: list[float], data_Y: list[float]) -> dict:
    length = len(data_X)
    data_X_mean = mean(
        data = data_X
    )
    data_Y_mean = mean(
        data = data_Y
    )
    nominator = 0
    denominator = 0
    for i in range(length):
        nominator = nominator + ( ( data_X[i] - data_X_mean ) * ( data_Y[i] - data_Y_mean ) )
        denominator = denominator + ( ( data_X[i] - data_X_mean ) ** 2 )
    response = {
        'a': nominator / denominator,
        'b': data_Y_mean - ( ( nominator / denominator ) * data_X_mean )
    }
    return response


def linear_regression(data_X: list[float], data_Y: list[float]) -> list[float]:
    params = linear_regression_params(
        data_X = data_X,
        data_Y = data_Y
    )
    a = params['a']
    b = params['b']
    Y_predicted = [ a * x + b for x in data_X ]
    return Y_predicted
