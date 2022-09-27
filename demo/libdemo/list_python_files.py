import os

allfiles = os.walk(r"c:\classroom\aug16\demo")
count = 0
for dirname, folders, files in allfiles:
    for file in files:
        if file.endswith(".py"):
            print(dirname + "\\" + file)
            count += 1

print("Count = ", count)
