# program to accept a number and display whether it is a perfect number or not

num = int(input("Enter the number: "))
total = 0
for i in range(1, num//2 + 1):
    if num % i == 0:
        total += i

if num == total:
    print("It is a perfect number.")
else:
    print("It is not a perfect number.")