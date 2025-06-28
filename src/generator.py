def linspace(a: float, b: float, size: int = 1000):
    response = []
    delta_x = ( b - a ) / size
    while a <= b:
        response.append(a)
        a = a + delta_x
    return response