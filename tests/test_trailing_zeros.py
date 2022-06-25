from assertpy import assert_that

from src.trailing_zeros import trailing_zeros
# Write a program that will calculate the number of trailing zeros in a factorial of a given number.

# N! = 1 * 2 * 3 * ... * N

# Be careful 1000! has 2568 digits...

# For more info, see: http://mathworld.wolfram.com/Factorial.html

# Examples
# zeros(6) = 1
# # 6! = 1 * 2 * 3 * 4 * 5 * 6 = 720 --> 1 trailing zero

# zeros(12) = 2
# # 12! = 479001600 --> 2 trailing zeros
# Hint: You're not meant to calculate the factorial. Find another way to find the number of zeros.

class TestTrailingZeros:
    
    def test_trailing_zeros_returns_the_number_of_zeros_at_the_final_of_the_number(self):
        assert_that(trailing_zeros(0)).is_equal_to(0)
        assert_that(trailing_zeros(6)).is_equal_to(1)
        assert_that(trailing_zeros(12)).is_equal_to(2)
        assert_that(trailing_zeros(30)).is_equal_to(7)
        assert_that(trailing_zeros(100)).is_equal_to(24)
        assert_that(trailing_zeros(1000)).is_equal_to(249)