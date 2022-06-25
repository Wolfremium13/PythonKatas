def is_valid(number: int) -> bool:
    digits = [int(x) for x in str(number)]
    for position_to_multiply in range(len(digits) - 2, -1, -2):
        digits[position_to_multiply] = sum(
            map(int, str(digits[position_to_multiply] * 2)))
    return sum(digits) % 10 == 0
