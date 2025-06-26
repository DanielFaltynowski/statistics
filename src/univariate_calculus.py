def derivative(f, x: float, delta_x: float = 0.0001) -> float:
    return ( f(x + delta_x) - f(x) ) / delta_x


def integral_rectangles_method(f, a: float, b: float, n: int = 100000) -> float:
    delta_x = (b - a) / n
    area = 0
    while a <= b:
        middle =  a + ( delta_x / 2 )
        area = area + ( delta_x * f(middle) )
        a = a + delta_x
    return area


def integral_trapezoidal_method(f, a: float, b: float, n: int = 100000) -> float:
    delta_x = (b - a) / n
    area = 0
    while a <= b:
        area = area + ( ( ( f(a) + f(a + delta_x) ) * delta_x ) / 2 )
        a = a + delta_x
    return area


def integral_simpsons_method(f, a: float, b: float, n: int = 100000) -> float:
    area = f(a) + f(b)
    delta_x = (b - a) / n
    i = 1
    while i < n:
        middle = a + ( i * delta_x )
        if i % 2 == 0:
            area = area + ( 2 * f(middle) )
        else:
            area = area + ( 4 * f(middle) )
        i = i + 1
    area = area * ( delta_x / 3 )
    return area

