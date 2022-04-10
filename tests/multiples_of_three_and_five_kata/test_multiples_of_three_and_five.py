from unittest import TestCase

from assertpy import assert_that

from src.multiples_of_three_and_five_kata.multiples_of_three_and_five import sum_of_multiples_of_three_and_five


class TestMultiplesOfThreeAndFive(TestCase):

    def test_returns_sum_multiples_of_three_and_five_given_positive_number(self):
        assert_that(sum_of_multiples_of_three_and_five(10)).is_equal_to(23)

    def test_returns_zero_given_zero(self):
        assert_that(sum_of_multiples_of_three_and_five(0)).is_equal_to(0)

    def test_returns_zero_given_negative_number(self):
        assert_that(sum_of_multiples_of_three_and_five(-1)).is_equal_to(0)
