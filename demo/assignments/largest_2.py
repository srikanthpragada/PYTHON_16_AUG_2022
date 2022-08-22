# Accept 3 numbers and display the largest of 3 numbers

number1 = int(input("Enter number 1: "))
number2 = int(input("Enter number 2: "))
number3 = int(input("Enter number 3: "))

largest = number1
if number2 > largest:
   largest = number2

if number3 > largest:
   largest = number3

print("The largest of the numbers is:", largest)