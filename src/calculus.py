def derivative(f: function, x: float, delta_x: float = 0.0001) -> float:
    return ( f(x + delta_x) - f(x) ) / delta_x


