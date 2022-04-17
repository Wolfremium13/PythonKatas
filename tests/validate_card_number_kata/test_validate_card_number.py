from unittest import TestCase

from assertpy import assert_that

from src.validate_card_number_kata.validate_card_number import _multiply_even_digits_from_final_by_two, \
    _sum_digits_mayor_than_nine, is_valid


class TestCardNumber(TestCase):

    # Should be removed, testing private method
    def test_multiply_digits_by_two_each_two_number_from_the_final_number(self):
        assert_that(_multiply_even_digits_from_final_by_two(1714)).is_equal_to([2, 7, 2, 4])
        assert_that(_multiply_even_digits_from_final_by_two(12345)).is_equal_to([1, 4, 3, 8, 5])
        assert_that(_multiply_even_digits_from_final_by_two(891)).is_equal_to([8, 18, 1])

    # Should be removed, testing private method
    def test_sum_digits_mayor_than_nine(self):
        assert_that(_sum_digits_mayor_than_nine([8, 18, 1])).is_equal_to([8, 9, 1])

    def test_is_valid_card_number_when_is_divisible_by_10(self):
        assert_that(is_valid(891)).is_false()
        assert_that(is_valid(2121)).is_true()
        assert_that(is_valid(1)).is_false()
