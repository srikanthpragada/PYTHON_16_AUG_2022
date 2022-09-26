with open("names.txt", "rt") as f:
    for name in sorted(f.readlines()):
        print(name.strip())  # print(name, end = '')
