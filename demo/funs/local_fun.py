g = 1


def f1():
    a = 100
    global g
    g = 100

    def f2():
        nonlocal a
        a = 200

    f2()
    print(a)


f1()
