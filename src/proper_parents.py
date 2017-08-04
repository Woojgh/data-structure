"""This will tell you if your string is all messed up."""


def pp(string):
    result = 0
    parens = False
    for char in string:
        if char in '()':
            parens = True
            if char == '(':
                result += 1
            else:
                result -= 1
                if result < 0:
                    return 'It\'s broken'
    if parens:
        return 'All balanced' if result == 0 else 'It\'s open'
    else:
        return 'No parents'
