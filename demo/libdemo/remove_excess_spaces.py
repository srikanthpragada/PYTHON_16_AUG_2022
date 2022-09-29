import re

with open("test.txt", 'rt') as f:
    contents = f.read()

newcontents = re.sub(r'  +', ' ', contents)

with open("test.txt", 'wt') as f:
    f.write(newcontents)
