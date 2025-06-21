def moment( data: list[ float ], centralisation: float = 0, standardisation: float = 1, k: int = 1 ) -> float:
    for datum in data:
        if not isinstance(datum, (int, float)):
            print('Invalid input: `moment(data)`')
            return None
    denominator = len( data )
    nominator = 0
    for datum in data:
        nominator = nominator + ( ( ( datum - centralisation ) / standardisation ) ** k )
    return nominator / denominator


def raw_moment( data: list[ float ], k: int = 1 ) -> float:
    return moment(
        data = data,
        centralisation = 0,
        standardisation = 1,
        k = k
    )


def centralised_moment( data: list[ float ], k: int = 1 ) -> float:
    return moment(
        data = data,
        centralisation = raw_moment(
            data = data,
            k = 1
        ),
        standardisation = 1,
        k = k
    )


def standardised_moment( data: list[ float ], k: int = 1 ) -> float:
    return moment(
        data = data,
        centralisation = raw_moment(
            data = data,
            k = 1
        ),
        standardisation = centralised_moment(
            data = data,
            k = 2
        ) ** 0.5,
        k = k
    )


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


def variance( data: list[ float ], from_sample = True ) -> float:
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


def standard_deviation( data: list[ float ], from_sample = True ) -> float:
    return variance( 
        data = data,
        from_sample = from_sample
     ) ** 0.5


def skewness( data: list[ float ], from_sample = True ) -> float:
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
        denominator = ( length - 1 ) * ( length - 2 )
    else:
        denominator = denominator * length
    return nominator / denominator


def kurtosis( data: list[ float ], from_sample = True ) -> float:
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
        denominator = ( length - 1 ) * ( length - 2 ) * ( length - 3 )
        substractor = ( ( 3 * ( ( length - 1 ) ** 2 ) ) / ( ( length - 2 ) * ( length - 3 ) ) )
    else:
        denominator = denominator * len( data )
    return ( nominator / denominator ) - substractor
    

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