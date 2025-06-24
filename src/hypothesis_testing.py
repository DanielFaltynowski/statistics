def benjamini_hockberg_method(p_values: list[float]) -> list[float]:
    reduced_p_values = p_values[:]
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