from assertpy import assert_that

from src.valid_parentheses import had_valid_parentheses
# Write a function that takes a string of parentheses, and determines if the order of the parentheses is valid.
#  The function should return true if the string is valid, and false if it's invalid.

# Examples
# "()" = >  true
# ")(()))" = >  false
# "text)" = >  false
# "(" = >  false
# "(())((()())())" = >  true
# Constraints
# 0 <= input.length <= 100

# Along with opening (() and closing ()) parenthesis, input may contain any valid ASCII characters.
# Furthermore, the input string may be empty and / or not contain any parentheses at all.
# Do not treat other forms of brackets as parentheses (e.g. [], {}, <> ).


class TestHadValidParentheses:

    def test_all_parentheses_have_opening_and_close(self):
        assert_that(had_valid_parentheses("")).is_true()
        assert_that(had_valid_parentheses("()")).is_true()
        assert_that(had_valid_parentheses("())")).is_false()
        assert_that(had_valid_parentheses("hi(hi)()")).is_true()
        assert_that(had_valid_parentheses("hi())(")).is_false()
        assert_that(had_valid_parentheses("(())((()())())")).is_true()
        assert_that(had_valid_parentheses(")fpv((s)s(p)")).is_false()
        assert_that(had_valid_parentheses("))(")).is_false()