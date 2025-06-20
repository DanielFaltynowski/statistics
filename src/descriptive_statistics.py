def moment( data: list[float], centralisation: float = 0, standardisation: float = 1, k: int = 1 ) -> float:
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


def raw_moment( data: list[float], k: int = 1 ) -> float:
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


def centralised_moment( data: list[float], k: int = 1 ) -> float:
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

def standardised_moment( data: list[float], k: int = 1) -> float:
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