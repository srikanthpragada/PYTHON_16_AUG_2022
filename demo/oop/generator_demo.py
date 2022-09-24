# Generator
def numbers():
    for n in range(1, 6):
        yield n


nums = numbers()
print(type(nums))
print(next(nums))
print(next(nums))

ge = (n for n in range(1, 6))   # Generator Expression
print(type(ge))
print(next(ge))
