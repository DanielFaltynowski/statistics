def moment(data: list[float], order: int = 1, delta_degrees_of_freedom: int = 0) -> float:
    for datum in data:
        if not isinstance(datum, (int, float)):
            print('Invalid input: `moment(data)`')
            return None
    degrees_of_freedom = len(data) - delta_degrees_of_freedom
    denominator = degrees_of_freedom
    nominator = 0
    for datum in data:
        nominator = nominator + ( datum ** order )
    return nominator / denominator


def centralised_moment(data: list[float], order: int = 1, delta_degrees_of_freedom: int = 0) -> float:
    for datum in data:
        if not isinstance(datum, (int, float)):
            print('Invalid input: `centralised_moment(data)`')
            return None
    degrees_of_freedom = len(data) - delta_degrees_of_freedom
    data_mean = moment(
        data = data,
    )
    denominator = degrees_of_freedom
    nominator = 0
    for datum in data:
        nominator = nominator + ( ( datum - data_mean ) ** order )
    return nominator / denominator


def standardised_moment(data: list[float], order: int = 1, delta_degrees_of_freedom: int = 0) -> float:
    for datum in data:
        if not isinstance(datum, (int, float)):
            print('Invalid input: `standardised_moment(data)`')
            return None
    degrees_of_freedom = len(data) - delta_degrees_of_freedom
    data_mean = moment(
        data = data,
    )
    data_sd = centralised_moment(
        data = data,
        order = 2,
        delta_degrees_of_freedom = delta_degrees_of_freedom
    ) ** 0.5
    denominator = degrees_of_freedom
    nominator = 0
    for datum in data:
        nominator = nominator + ( ( ( datum - data_mean ) ** order ) / ( data_sd ** order ) )
    return nominator / denominator


def mean( data: list[ float ] ) -> float:
    for datum in data:
        if not isinstance(datum, (int, float)):
            print('Invalid input: `mean(data)`')
            return None
    length = len( data )
    denominator = length
    nominator = 0
    for datum in data:
        nominator = nominator + datum
    return nominator / denominator


def variance( data: list[ float ], from_sample: bool = True ) -> float:
    for datum in data:
        if not isinstance(datum, (int, float)):
            print('Invalid input: `variance(data)`')
            return None
    length = len( data )
    denominator = length
    data_mean = mean( data )
    if from_sample:
        denominator = denominator - 1
    nominator = 0
    for datum in data:
        nominator = nominator + ( ( datum - data_mean ) ** 2 )
    return nominator / denominator


def standard_deviation( data: list[ float ], from_sample: bool = True ) -> float:
    return variance( 
        data = data,
        from_sample = from_sample
     ) ** 0.5


def skewness( data: list[ float ], from_sample: bool = True ) -> float:
    for datum in data:
        if not isinstance(datum, (int, float)):
            print('Invalid input: `skewness(data)`')
            return None
    length = len( data )
    denominator = standard_deviation(
        data = data,
        from_sample = from_sample
    ) ** 3
    nominator = 0
    data_mean = mean( data )
    for datum in data:
        nominator = nominator + ( ( datum - data_mean ) ** 3 )
    if from_sample:
        nominator = nominator * length
        denominator = denominator * ( length - 1 ) * ( length - 2 )
    else:
        denominator = denominator * length
    return nominator / denominator


def kurtosis( data: list[ float ], from_sample: bool = True ) -> float:
    for datum in data:
        if not isinstance(datum, (int, float)):
            print('Invalid input: `kurtosis(data)`')
            return None
    length = len( data )
    denominator = standard_deviation(
        data = data,
        from_sample = from_sample
    ) ** 4
    nominator = 0
    data_mean = mean( data )
    for datum in data:
        nominator = nominator + ( ( datum - data_mean ) ** 4 )
    substractor = 0
    if from_sample:
        nominator = nominator * length * ( length + 1 )
        denominator = denominator * ( length - 1 ) * ( length - 2 ) * ( length - 3 )
        substractor = ( ( 3 * ( ( length - 1 ) ** 2 ) ) / ( ( length - 2 ) * ( length - 3 ) ) ) - 3
    else:
        denominator = denominator * len( data )
    return ( nominator / denominator ) - substractor


def excess_kurtosis( data: list[ float ], from_sample: bool = True ) -> float:
    return kurtosis(
        data = data,
        from_sample = from_sample
    ) - 3
    

def median(data: list[float]) -> float:
    for datum in data:
        if not isinstance(datum, (int, float)):
            print('Invalid input: `median(data)`')
            return None
    data_sorted = data[ : ]
    data_sorted.sort()
    last_index = len( data ) - 1
    if last_index % 2 == 0:
        return data_sorted[ last_index // 2 ]
    else:
        first_point = data_sorted[ last_index // 2 ]
        second_point = data_sorted[ last_index // 2 + 1 ]
        return ( first_point + second_point ) / 2


def mode(data: list[float]) -> float:
    for datum in data:
        if not isinstance(datum, (int, float)):
            print('Invalid input: `mode(data)`')
            return None
    memory = {}
    for datum in data:
        if datum in memory:
            memory[datum] = memory[datum] + 1
        else:
            memory[datum] = 1
    mode = None
    max_amount = 0
    for value, amount in memory.items():
        if amount > max_amount:
            max_amount = amount
            mode = value
    modes = []
    for value, amount in memory.items():
        if amount == max_amount:
            modes.append( value )
    if len(modes) > 1:
        return modes
    else:
        return mode


def data_range(data: list[float]) -> tuple[float]:
    for datum in data:
        if not isinstance(datum, (int, float)):
            print('Invalid input: `data_range(data)`')
            return None
    min_value = data[0]
    max_value = data[0]
    for datum in data:
        if datum < min_value:
            min_value = datum
        if datum > max_value:
            max_value = datum
    return (min_value, max_value)


def standard_error(data: list[float]) -> float:
    for datum in data:
        if not isinstance(datum, (int, float)):
            print('Invalid input: `standard_error(data)`')
            return None
    length = len(data)
    return standard_deviation(data = data) / ( length ** 0.5 )


def weighted_mean( data: list[ float ], weights: list[int] ) -> float:
    for datum in data:
        if not ( isinstance(datum, (int, float)) and len(data) == len(weights) ):
            print('Invalid input: `weighted_mean(data)`')
            return None
    for weight in weights:
        if not ( isinstance(weight, (int, float)) and weight >= 0 ):
            print('Invalid input: `weighted_mean(data)`')
            return None
    length = len( data )
    denominator = 0
    nominator = 0
    for i in range(length):
        nominator = nominator + ( data[i] * weights[i] )
        denominator = denominator + weights[i]
    return nominator / denominator


def weighted_variance( data: list[ float ], weights: list[int], from_sample: bool = True ) -> float:
    for datum in data:
        if not ( isinstance(datum, (int, float)) and len(data) == len(weights) ):
            print('Invalid input: `weighted_variance(data)`')
            return None
    for weight in weights:
        if not ( isinstance(weight, (int, float)) and weight >= 0 ):
            print('Invalid input: `weighted_variance(data)`')
            return None
    length = len( data )
    weights_sum = 0
    squared_weights_sum = 0
    for i in range(length):
        weights_sum = weights_sum + weights[i]
        squared_weights_sum = squared_weights_sum + ( weights[i] ** 2 )
    denominator = weights_sum
    data_mean = weighted_mean( 
        data = data,
        weights = weights,
     )
    if from_sample:
        denominator = denominator - ( squared_weights_sum / weights_sum )
    nominator = 0
    for i in range(length):
        nominator = nominator + weights[i] * ( ( data[i] - data_mean ) ** 2 )
    return nominator / denominator


def weighted_standard_deviation( data: list[ float ], weights: list[int], from_sample: bool = True ) -> float:
    return weighted_variance( 
        data = data,
        weights = weights,
        from_sample = from_sample
     ) ** 0.5


def weighted_skewness( data: list[ float ], weights: list[int], from_sample: bool = True ) -> float:
    for datum in data:
        if not ( isinstance(datum, (int, float)) and len(data) == len(weights) ):
            print('Invalid input: `weighted_skewness(data)`')
            return None
    for weight in weights:
        if not ( isinstance(weight, (int, float)) and weight >= 0 ):
            print('Invalid input: `weighted_skewness(data)`')
            return None
    length = len( data )
    weights_sum = 0
    squared_weights_sum = 0
    for i in range(length):
        weights_sum = weights_sum + weights[i]
        squared_weights_sum = squared_weights_sum + ( weights[i] ** 2 )
    denominator = weighted_standard_deviation(
        data = data,
        weights = weights,
        from_sample = from_sample
    ) ** 3
    denominator = denominator * weights_sum
    data_mean = weighted_mean( 
        data = data,
        weights = weights
     )
    nominator = 0
    for i in range(length):
        nominator = nominator + weights[i] * ( ( data[i] - data_mean ) ** 3 )
    if from_sample:
        return weighted_skewness(
            data = data,
            weights = weights,
            from_sample = False
        ) * ( weights_sum / ( weights_sum - ( squared_weights_sum / weights_sum ) ) )
    else:
        return nominator / denominator


def weighted_kurtosis( data: list[ float ], weights: list[int], from_sample: bool = True ) -> float:
    for datum in data:
        if not ( isinstance(datum, (int, float)) and len(data) == len(weights) ):
            print('Invalid input: `weighted_kurtosis(data)`')
            return None
    for weight in weights:
        if not ( isinstance(weight, (int, float)) and weight >= 0 ):
            print('Invalid input: `weighted_kurtosis(data)`')
            return None
    length = len( data )
    weights_sum = 0
    squared_weights_sum = 0
    for i in range(length):
        weights_sum = weights_sum + weights[i]
        squared_weights_sum = squared_weights_sum + ( weights[i] ** 2 )
    denominator = weighted_standard_deviation(
        data = data,
        weights = weights,
        from_sample = from_sample
    ) ** 4
    denominator = denominator * weights_sum
    data_mean = weighted_mean( 
        data = data,
        weights = weights
     )
    nominator = 0
    for i in range(length):
        nominator = nominator + weights[i] * ( ( data[i] - data_mean ) ** 4 )
    if from_sample:
        return ( ( weighted_kurtosis(
            data = data,
            weights = weights,
            from_sample = False
        ) - 3) + 3 ) * ( weights_sum / ( weights_sum - ( squared_weights_sum / weights_sum ) ) )
    else:
        return nominator / denominator


def weighted_excess_kurtosis( data: list[ float ], weights: list[int], from_sample: bool = True ) -> float:
    return weighted_kurtosis(
        data = data,
        weights = weights,
        from_sample = from_sample
    ) - 3


def weighted_median(data: list[float], weights: list[float]) -> float:
    for datum in data:
        if not ( isinstance(datum, (int, float)) and len(data) == len(weights) ):
            print('Invalid input: `weighted_kurtosis(data)`')
            return None
    for weight in weights:
        if not ( isinstance(weight, (int, float)) and weight >= 0 ):
            print('Invalid input: `weighted_kurtosis(data)`')
            return None
    sorted_pairs = sorted(zip(data, weights), key=lambda x: x[0])
    total_weight = 0
    for weight in weights:
        total_weight = total_weight + weight
    half_weight = total_weight / 2
    cumulative_weight = 0
    for value, weight in sorted_pairs:
        cumulative_weight = cumulative_weight + weight
        if cumulative_weight >= half_weight:
            return value
    return None



def weighted_mode(data: list[float], weights: list[int]) -> float:
    for datum in data:
        if not ( isinstance(datum, (int, float)) and len(data) == len(weights) ):
            print('Invalid input: `weighted_mode(data)`')
            return None
    for weight in weights:
        if not ( isinstance(weight, (int, float)) and weight >= 0 ):
            print('Invalid input: `weighted_mode(data)`')
            return None
    length = len(data)
    mode = data[0]
    weight = weights[0]
    for i in range(length):
        if weights[i] > weight:
            mode = data[i]
            weight = weights[i]
    modes = []
    for i in range(length):
        if weights[i] == weight:
            modes.append(data[i])
    if len(modes) > 1:
        return modes
    else:
        return mode


def weighted_standard_error(data: list[float], weights: list[int]) -> float:
    for datum in data:
        if not ( isinstance(datum, (int, float)) and len(data) == len(weights) ):
            print('Invalid input: `weighted_standard_error(data)`')
            return None
    for weight in weights:
        if not ( isinstance(weight, (int, float)) and weight >= 0 ):
            print('Invalid input: `weighted_standard_error(data)`')
            return None
    sum_of_weights = 0
    for weight in weights:
        sum_of_weights = sum_of_weights + weight
    return weighted_standard_deviation(data = data, weights = weights) / ( len(data) ** 0.5 )