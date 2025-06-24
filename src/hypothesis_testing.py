def benjamini_hockberg_method(p_values: list[float]) -> list[float]:
    for p_value in p_values:
        if not isinstance(p_value, (int, float)) or not 0 <= p_value <= 1:
            print('Invalid Input `benjamini_hockberg_method(p_values)`')
    reduced_p_values = p_values[:]
    reduced_p_values.sort()
    length = len(p_values)
    i = length - 2
    while i >= 0:
        bh = reduced_p_values[i] * ( length / ( i + 1 ) )
        if bh < reduced_p_values[i + 1]:
            reduced_p_values[i] = bh
        else:
            reduced_p_values[i] = reduced_p_values[i + 1]
        i = i - 1
    return reduced_p_values