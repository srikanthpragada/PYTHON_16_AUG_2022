def ispositive(n) -> bool:
    return n >= 0


nums = [10, -20, 30, -5, 50]

for n in filter(ispositive, nums):
    print(n)


for c in filter(str.isdigit, "Abc12Xy45"):
    print(c)