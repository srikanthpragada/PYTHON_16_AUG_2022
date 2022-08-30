def hello(name: str, msg: str):
    print(msg, name)


hello("Ben", "Hello")  # Positional args
hello(msg="Good Morning", name="Steve")  # keyword args

