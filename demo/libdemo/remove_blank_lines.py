with open("names.txt", "rt") as f:
    lines = []
    for line in f.readlines():
        if len(line.strip()) > 0:
            lines.append(line)


with open("names.txt", "wt") as f:
    for line in lines:
        f.write(line)