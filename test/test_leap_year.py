from assertpy import assert_that
from src.leap_year import is_leap_year


class TestIsLeapYear:
    def test_is_leap_year_when_is_divisible_by_four(self):
        assert_that(is_leap_year(4)).is_equal_to(True)
        assert_that(is_leap_year(5)).is_equal_to(False)

    def test_is_leap_year_when_is_divisible_by_four_hundred(self):
        assert_that(is_leap_year(400)).is_equal_to(True)
        assert_that(is_leap_year(503)).is_equal_to(False)

    def test_is_leap_year_when_is_divisible_by_one_hundred_but_not_for_four_hundred(self):
        assert_that(is_leap_year(1800)).is_equal_to(False)
        assert_that(is_leap_year(1600)).is_equal_to(True)
