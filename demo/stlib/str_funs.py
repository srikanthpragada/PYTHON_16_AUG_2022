def has_upper(s):
    for c in s:
        if c.isupper():
            return True

    return False


def count_upper(s):
    count = 0
    for c in s:
        if c.isupper():
            count += 1

    return count
