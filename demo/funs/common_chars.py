def common_chars(s1, s2):
    return "".join(set(s1) & set(s2))


def common_chars2(st1: str, st2: str) -> str:
    com_chars = ""
    for c in st1:
        if c in st2 and c not in com_chars:
            com_chars += c

    return com_chars


print(common_chars('how are you', 'how do you do'))
print(common_chars2('how are you', 'how do you do'))
