def bootstrapp(data: list[float]) -> list[float]:
    import random
    length = len(data)
    bootstrapped_data = []
    for i in range(length):
        random_index = random.randrange(0, length)
        bootstrapped_data.append(data[random_index])
    return bootstrapped_data