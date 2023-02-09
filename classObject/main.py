class BankAccount:
    def set_details(self,name,balance=0):
        self.name = name
        self.balance = balance

    def display(self):
        print(self.name)
        print(self.balance)

    def withdraw(self, amount):
        self.balance -=amount

    def deposit(self, amount):
        self.balance += amount


a1 = BankAccount()
a2 = BankAccount()

a1.set_details('Tareq')
a1.display()
a1.deposit(500)
a1.display()
a1.deposit(1000)
a1.display()
a1.withdraw(1000)
a1.display()
a1.withdraw(150)
a1.display()

a2.set_details('Annan')
a2.deposit(1500)
a2.display()





"""Quiz"""
# class Boy:
#     pass
#
# t1 = Boy()
# t2 = Boy()
#
# print(t1 == t2, end=' ')
# print(type(t1) == type(t2),end=' ')
#

# class Test:
#     def method1(self):
#         print('Inside method1')
#
#     def method2(self):
#         print('Inside method2')
#         self.method1()
#
#
# t = Test()
# t.method1()
# t1 =Test()
# t1.method2()
#
# class Test:
#     def method1(self):
#         self.x = 10
#
#     def display(self):
#         print(self.x)
#
#
# t = Test()
# t.method1()
# t.display()

# class Test:
#     def method1(self, x):
#         self.x = x
#
#     def method2(self):
#         self.x += 10
#
#     def display(self):
#         print(self.x)
#
#
# t = Test()
# t.method1(5)
# t.method2()
# t.display()