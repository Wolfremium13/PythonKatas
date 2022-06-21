import re


def increment_the_end_number_by_one(input: str) -> str:
    matched_digits = re.match('.*?([0-9]+)$', input)
    if not matched_digits:
        return input + "1"

    end_digits = [d for d in matched_digits.group(1)]
    result = int(''.join(end_digits)) + 1
    result_digits = [d for d in str(result)]
    replaced_digits = end_digits[:len(result_digits) * -1] + result_digits

    input_characters = [c for c in input]
    difference = len(replaced_digits) - len(end_digits)
    replaced_input = input_characters[:(len(
        replaced_digits) - difference) * -1] + replaced_digits

    return ''.join(replaced_input)
