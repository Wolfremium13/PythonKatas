from unittest import TestCase

from assertpy import assert_that

from src.validate_card_number_kata.validate_card_number import is_valid


class TestCardNumber(TestCase):

    def test_is_valid_card_number_when_is_divisible_by_10(self):
        assert_that(is_valid(891)).is_false()
        assert_that(is_valid(2121)).is_true()
        assert_that(is_valid(1)).is_false()
