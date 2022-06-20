def had_valid_parentheses(input: str) -> bool:
    valid_parentheses_values = ['(', ')']
    parentheses = [p for p in input if p in valid_parentheses_values]
    return _had_the_same_pairs(parentheses)


def _had_the_same_pairs(parentheses) -> bool:
    open_parentheses = '('
    close_parentheses = ')'
    if not parentheses:
        return True

    if parentheses[0] is close_parentheses or not close_parentheses in parentheses[0:]:
        return False

    if parentheses[0] is open_parentheses and close_parentheses in parentheses[0:]:
        parentheses.remove(parentheses[0])
        parentheses.pop(parentheses[0:].index(close_parentheses))
    return _had_the_same_pairs(parentheses)
