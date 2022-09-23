class FundsError(Exception):
    def __init__(self, balance, amount):
        self.__message = f"Available balance is {balance}, but withdraw amount is {amount}"

    def __str__(self):
        return self.__message


class Account:
    # Constructor
    def __init__(self, acno, ahname, balance=0):
        # object attributes
        self.acno = acno
        self.ahname = ahname
        self.balance = balance

    # Methods
    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance < amount:
            raise FundsError(self.balance, amount)

        self.balance -= amount

    def getbalance(self):
        return self.balance

    # Returns a string from object data
    def __str__(self):
        return f"{self.acno} - {self.ahname} - {self.balance}"


a1 = Account(1, "Scott")
a1.deposit(10000)
a1.deposit(20000)

print(a1.getbalance())
print(a1)  # a1.__str__

a2 = Account(2, "Tom", 20000)
try:
    a2.withdraw(30000)
except FundsError as ex:
    print(ex)
