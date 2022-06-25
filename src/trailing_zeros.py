from math import floor


def trailing_zeros(given_number: int) -> int:
    divider = 5
    divider_factorial = divider
    result = 0
    calculation = floor(given_number / divider_factorial)
    calculation_is_positive = calculation > 0
    while calculation_is_positive:
        result += calculation
        divider_factorial *= divider
    return result
