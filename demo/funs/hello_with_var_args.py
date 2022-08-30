def hello(*names, msg: str = 'Hello'):
    for n in names:
        print(msg, n)


hello('Tom', 'Steve', 'James')
hello('Larry', 'Bill', msg='Hi')
