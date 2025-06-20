def moment( data: list[ float ], centralisation: float = 0, standardisation: float = 1, k: int = 1 ) -> float:
    """
    Calculates the k-th moment of the data with optional centralisation and standardisation.
    
    Parameters:
    data (list of float): The dataset values.
    centralisation (float): The value to centralise data around (default is 0).
    standardisation (float): The value to standardise data by (default is 1).
    k (int): The order of the moment to calculate.
    
    Returns:
    float: The k-th moment of the data.
    """
    denominator = len( data )
    nominator = 0
    for datum in data:
        nominator = nominator + ( ( ( datum - centralisation ) / standardisation ) ** k )
    return nominator / denominator


def raw_moment( data: list[ float ], k: int = 1 ) -> float:
    """
    Calculates the raw (non-centralised) k-th moment of the data.
    
    Parameters:
    data (list of float): The dataset values.
    k (int): The order of the moment to calculate.
    
    Returns:
    float: The raw k-th moment of the data.
    """
    return moment(
        data = data,
        centralisation = 0,
        standardisation = 1,
        k = k
    )


def centralised_moment( data: list[ float ], k: int = 1 ) -> float:
    """
    Calculates the centralised k-th moment of the data (moment about the mean).
    
    Parameters:
    data (list of float): The dataset values.
    k (int): The order of the moment to calculate.
    
    Returns:
    float: The centralised k-th moment of the data.
    """
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
    """
    Calculates the standardised k-th moment of the data (centralised and divided by standard deviation).
    
    Parameters:
    data (list of float): The dataset values.
    k (int): The order of the moment to calculate.
    
    Returns:
    float: The standardised k-th moment of the data.
    """
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
    length = len( data )
    denominator = length
    nominator = 0
    for datum in data:
        nominator = nominator + datum
    return nominator / denominator


def variance( data: list[ float ], from_sample = True ) -> float:
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
    
