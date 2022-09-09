# Accept a number on command line and display its factors

import sys

#print(sys.argv)

if len(sys.argv) < 2:
    print("Number is missing!")
    print("Please run >python factors.py number")
    exit()

number = int(sys.argv[1])

for i in range(2, number // 2 + 1):
    if number % i == 0:
        print(i)
