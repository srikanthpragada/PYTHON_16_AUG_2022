# program to print the smallest factor of a number other than 1
# in case we don't have a factor then print the number itself

num = int(input("Enter the number: "))
for i in range(2, num // 2 + 1):
    if num % i == 0:
        print(i)
        break
else:
    print(num)
