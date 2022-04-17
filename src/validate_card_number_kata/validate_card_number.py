def is_valid(number: int) -> bool:
    digits = _multiply_even_digits_from_final_by_two(number)
    return sum(_sum_digits_mayor_than_nine(digits)) % 10 == 0


def _multiply_even_digits_from_final_by_two(number: int) -> list:
    digits = [int(digit) for digit in str(number)]
    card_position = len(digits) - 2
    while card_position >= 0:
        digits[card_position] *= 2
        card_position -= 2
    return digits


def _sum_digits_mayor_than_nine(digits: list) -> list:
    for i in range(len(digits)):
        if digits[i] > 9:
            digits[i] = sum([int(d) for d in str(digits[i])])
    return digits
