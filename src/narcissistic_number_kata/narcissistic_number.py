import functools


def is_narcissistic(given_number: int) -> bool:
    digits = [int(n) for n in str(given_number)]
    calculated_digits = list(map(lambda d: pow(d, len(digits)), digits))
    sum_of_digits = functools.reduce(lambda a, b: a + b, calculated_digits)
    return sum_of_digits == given_number
