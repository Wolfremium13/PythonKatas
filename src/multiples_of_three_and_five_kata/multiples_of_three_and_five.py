import functools


def sum_of_multiples_of_three_and_five(given_number: int) -> int:
    if given_number <= 0:
        return 0

    possible_numbers = [n for n in range(given_number)]
    multiples_of_three_and_five = filter(lambda n: n % 3 == 0 or n % 5 == 0, possible_numbers)
    return functools.reduce(lambda a, b: a + b, multiples_of_three_and_five)
