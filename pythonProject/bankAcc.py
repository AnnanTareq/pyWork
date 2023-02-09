"""class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.__balance = balance

    @property
    def set_details(self):
        return self.name, self.__balance

    @set_details.setter
    def set_details(self, val):
        self.__balance += val

    @set_details.deleter
    def set_details(self):
        print('Value has been deleted')

    def display(self):
        print(self.name)
        print(self.__balance)

    def deposit(self, val):
        self.__balance += val

    def withdraw(self, amount):
        self.__balance -= amount


b1 = BankAccount('Tareq Annan', 1200)

b1.display()
b1.deposit(500)
b1.display()

b1.display()
del b1.set_details

b1.display()

"""


class bankAcc:
    def __init__(self, name, balance=500):
        self.name = name
        self.balance = balance

    def deposit(self, val):
        self.balance += val

    def withdraw(self, val):
        self.balance -= val

    def display(self):
        print(self.name)
        print(self.balance)


b2 = bankAcc('Joy')
b2.deposit(500)
b2.display()