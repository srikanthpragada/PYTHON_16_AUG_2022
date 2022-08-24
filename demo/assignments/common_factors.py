# Accept 2 numbers and display common factors

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

smaller = num1 if num1 < num2 else num2

for i in range(1, smaller // 2 + 1):
    if num1 % i == 0 and num2 % i == 0:
        print(i)
