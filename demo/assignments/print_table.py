# program to accept a number and display a table for that number

num = int(input("Enter the number: "))
for n in range(1, 11):
    print(f"{num:3}  *  {n:2}  =  {num * n:5}")
