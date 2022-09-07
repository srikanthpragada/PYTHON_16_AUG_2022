def unique_chars(s):
    chars = []
    for c in s:
        if c not in chars:
            chars.append(c)

    return "".join(chars)  # convert list to str


nums = [10, -20, 30, -5, 50]
names = ['Java', 'Python', 'C++']

for n in map(abs, nums):
    print(n)

for n in map(unique_chars, names):
    print(n)

for l in map(len, names):
    print(l)
