class BankAccount:
    Bank_name = 'AB Bank, Bashundhara, Dhaka'

    def __init__(self, name, balance = 0, bank = Bank_name):
        self.name = name
        self.balance = balance
        self.bank = bank

    def display(self):
        print(self.name, self.balance, self.bank)

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount


a1 = BankAccount('Mike', 200, 'PQR Bank')
a2 = BankAccount('Tom')

a1.display()
a2.display()