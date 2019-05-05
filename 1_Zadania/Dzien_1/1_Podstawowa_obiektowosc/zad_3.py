class BankAccount:

    def __init__(self, number):
        self.number = number
        self.cash = 0.0

    def deposit_cash(self, amount):
        if amount > 0:
            self.cash += amount

    def withdraw_cash(self, amount):
        if amount > self.cash:
            r = amount - self.cash
            self.cash = 0.0
            return r
        else:
            self.cash -= amount
            return amount

    def print_info(self):
        print("nr konta: {}, ilość kasy {}" .format(self.number, self.cash))

a1 = BankAccount(1234)
a1.deposit_cash(600)
print(a1.withdraw_cash(200))
a1.print_info()