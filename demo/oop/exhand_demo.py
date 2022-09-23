a = input("Enter number :")
try:
    b = int(a)
    print(100 // b)
except ValueError as ex:
    print("Sorry! Input is not a number.")
# except ZeroDivisionError:
#     print("Sorry! Zero is not valid as number.")
except Exception as ex:
    print("Error -->", ex)
else:
    print("Normal end")
finally:
    print("Finally block")


print("The End")
