# Accept a number and display whether it is a prime number

number = int(input("Enter a number: "))

for i in range(2, number // 2 + 1):
    if number % i == 0:
        print("Not a prime number")
        break
else:
    print("Prime number")
