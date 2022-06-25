from math import floor


def trailing_zeros(given_number: int) -> int:
    divider = 5
    divider_factorial = divider
    result = 0
    while floor(given_number / divider_factorial) > 0:
        result += floor(given_number / divider_factorial)
        divider_factorial *= divider
    return result
