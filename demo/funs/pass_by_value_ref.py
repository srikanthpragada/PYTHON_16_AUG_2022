def zero(n):
    print(id(n), n)
    n = 0
    print(id(n), n)


def prepend(lst, value):
    lst.insert(0, value)


a = 100
print(id(a))
zero(a)
print(a)

l = [10,20]
prepend(l, 5)
print(l)