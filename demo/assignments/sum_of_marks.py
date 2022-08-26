# program to accept a string which contains numbers or characters separated by comma
# print the sum of those numbers

nums = "10,15,20,25,c,30"
total = 0
for n in nums.split(","):
    if n.isdigit():
        total += int(n)

print(total)
