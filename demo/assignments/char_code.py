# accept a string and display each character along with its ASCII code

s = input("Enter the string: ")
for c in s:
    print(f"{c} {ord(c)}")
