# program to a string and display each word on a separate line

s = "How you doing?"
for c in s:
    if c == " ":
        print()   # new line
    else:
        print(c, end="")