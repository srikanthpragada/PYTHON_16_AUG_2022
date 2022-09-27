import os

FILENAME = "names.txt"
TEMPFILE = "temp.txt"
with open(FILENAME, "rt") as f, open(TEMPFILE, "wt") as tf:
    for line in f.readlines():
        if len(line.strip()) > 0:
            tf.write(line)

os.remove(FILENAME)
os.rename(TEMPFILE, FILENAME)
