def iseven(n):
    return n % 2 == 0


def ispositive(n):
    return n > 0


if __name__ == '__main__':  # name of the module is __main__ when run as script
    print("Math Functions Ver 1.0")
    print(iseven(10), ispositive(-10))
