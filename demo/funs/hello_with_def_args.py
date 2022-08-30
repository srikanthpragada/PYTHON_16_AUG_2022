def hello(name: str = 'Guest', msg: str = 'Hello'):
    print(msg, name)


hello("Ben")  # Positional args
hello(msg="Good Morning", name="Steve")  # keyword args
hello(name = 'Tom')
hello()
hello(msg = 'Hi')
