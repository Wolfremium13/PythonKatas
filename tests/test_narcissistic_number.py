from assertpy import assert_that

from src.narcissistic_number import is_narcissistic

#  Narcissistic Number Kata

# A [Narcissistic Number](https://en.wikipedia.org/wiki/Narcissistic_number) is a positive number which is the sum of its
# own digits, each raised to the power of the number of digits in a given base. In this Kata, we will restrict ourselves
# to decimal (base 10).

# For example, take 153 (3 digits), which is narcissistic:

# ```
#    1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
# ```

# and 1652 (4 digits), which isn't:

# ```
#    1^4 + 6^4 + 5^4 + 2^4 = 1 + 1296 + 625 + 16 = 1938
# ```

# The Challenge:

# Your code must return true or false (not 'true' and 'false') depending upon whether the given number is a Narcissistic
# number in base 10. This may be `True` and `False` in your language.

# > Error checking for text strings or other invalid inputs is not required, only valid positive non-zero integers will be passed into the function.

# [Codewars kata](https://www.codewars.com/kata/5287e858c6b5a9678200083c)


class TestIsNarcissisticNumber:
    def test_is_narcissistic_number_returns_false_given_not_a_narcissistic_one(self):
        assert_that(is_narcissistic(150)).is_false()

    def test_is_narcissistic_returns_true_given_zero(self):
        assert_that(is_narcissistic(0)).is_true()

    def test_is_narcissistic_number_returns_true_given_narcissistic_one(self):
        assert_that(is_narcissistic(153)).is_true()
