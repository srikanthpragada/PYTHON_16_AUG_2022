def upper_count(st: str) -> int:
    count = 0
    for c in st:
        if c.isupper():
            count += 1

    return count


def has_upper(st: str) -> bool:
    for c in st:
        if c.isupper():
            return True

    return False


c = upper_count('Hello! How Are You')
print(c)
c = upper_count('hello')
print(c)
print(has_upper('abc'), has_upper('aBc'))

