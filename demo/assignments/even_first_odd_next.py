# program to accept numbers and display first even and then odd numbers

evens, odds = [], []
while True:
    num = int(input("Enter the number [0 to end]: "))
    if num == 0:
        break

    if num % 2 == 0:
        evens.append(num)
    else:
        odds.append(num)

print(evens + odds)
