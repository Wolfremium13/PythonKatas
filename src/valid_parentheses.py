def had_valid_parentheses(line: str) -> bool:
    counter = 0
    for character in line:
        if character == '(':
            counter += 1
        if character == ')':
            counter -= 1
        if counter < 0:
            return False
    return True if counter == 0 else False
