def greater_or_equal_power_of_two(n: int):
    if n < 2:
        raise ValueError("The number must be at least 2.")
    result = 2
    while result < n:
        result *= 2
    return result