import re

with open("test.txt", 'rt') as f:
    contents = f.read()

words = re.findall(r'\w+', contents)
for w in sorted(set(words)):
    print(f"{w:15}  {words.count(w)}")
