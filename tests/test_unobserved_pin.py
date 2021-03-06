from assertpy import assert_that

from src.unobserved_pin import get_pins

# Alright, detective, one of our colleagues successfully observed our target person,
# Robby the robber. We followed him to a secret warehouse, where we assume to find all
# the stolen stuff. The door to this warehouse is secured by an electronic combination lock.
# Unfortunately our spy isn't sure about the PIN he saw, when Robby entered it.

# The keypad has the following layout:

# ┌───┬───┬───┐image.png
# │ 1 │ 2 │ 3 │
# ├───┼───┼───┤
# │ 4 │ 5 │ 6 │
# ├───┼───┼───┤
# │ 7 │ 8 │ 9 │
# └───┼───┼───┘
#     │ 0 │
#     └───┘
# He noted the PIN 1357, but he also said, it is possible that each of the digits
# he saw could actually be another adjacent
# digit (horizontally or vertically, but not diagonally).
# E.g. instead of the 1 it could also be the 2 or 4.
# And instead of the 5 it could also be the 2, 4, 6 or 8.

# He also mentioned, he knows this kind of locks. You can enter an
# unlimited amount of wrong PINs, they never finally lock the system or sound the alarm.
# That's why we can try out all possible (*) variations.

# * possible in sense of: the observed PIN itself and all variations
# considering the adjacent digits

# Can you help us to find all those variations? It would be nice to
# have a function, that returns an array (or a list in Java/Kotlin and C#)
# of all variations for an observed PIN with a length of 1 to 8 digits.
# We could name the function getPINs (get_pins in python, GetPINs in C#).
# But please note that all PINs, the observed one and also the results,
# must be strings, because of potentially leading '0's.
# We already prepared some test cases for you.

# Detective, we are counting on you!


class TestUnobservedPin:
    def test_returns_adjacent_numbers(self):
        assert_that(get_pins('0')).is_equal_to(['0', '8'])
        assert_that(get_pins('1')).is_equal_to(['1', '2', '4'])
        assert_that(get_pins('2')).is_equal_to(['2', '1', '3', '5'])
        assert_that(get_pins('3')).is_equal_to(['3', '2', '6'])

    def test_returns_all_combinations_from_given_number(self):
        assert_that(get_pins('369')).is_equal_to(
            [
                '256', '258', '259', '266', '268', '269', '296',
                '298', '299', '236', '238', '239', '356', '358',
                '359', '366', '368', '369', '396', '398', '399',
                '336', '338', '339', '656', '658', '659', '666',
                '668', '669', '696', '698', '699', '636', '638',
                '639'
            ]
        )
