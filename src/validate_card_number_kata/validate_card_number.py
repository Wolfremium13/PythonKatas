def is_valid(number: int) -> bool:
    digits = [int(x) for x in str(number)]
    for digit in range(len(digits) - 2, -1, -2):
        digits[digit] = sum(map(int, str(digits[digit] * 2)))
    return sum(digits) % 10 == 0
