# Done
def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """
    items = 0
    for ch in parens:
        if ch == '(':
            items = items + 1
        if ch == ')':
            items = items - 1
        if items < 0:
            return False
    if items != 0:
        return False
    return True