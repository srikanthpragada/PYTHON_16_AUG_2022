def has_upper(s):
    """
    Returns true if the given string has any uppercase letter
    :param s: Source string
    :return: True if uppercase found, False otherwise
    """
    for c in s:
        if c.isupper():
            return True

    return False


def count_upper(s):
    """
    Returns number of uppercase letters in the given string
    :param s: Source string
    :return:  Count of uppercase letters
    """
    count = 0
    for c in s:
        if c.isupper():
            count += 1

    return count
