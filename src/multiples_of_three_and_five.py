def sum_of_multiples_of_three_and_five(given_number: int) -> int:
    return sum(x for x in range(given_number) if x % 3 == 0 or x % 5 == 0)
