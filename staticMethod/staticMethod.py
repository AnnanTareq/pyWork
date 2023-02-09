"""class Date:
    def __init__(self, d, m, y):
        self.d = d
        self.m = m
        self.y = y

    def is_valid(self):
        pass

    def add_days(self, days):
        pass

    def find_weekday(self):
        pass

    @staticmethod
    def is_leap(year):
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            print('Yes')
        else:
            print('No')


a1 = Date(20, 4, 2022)
Date.is_leap(2019)
"""


class StatMethod:

    a = 5

    def __init__(self,x):
        self.x = x

    def method1(self):
        print(self.x)

    @classmethod
    def method2(cls):
        print(cls.a)

    @staticmethod
    def method3(x, y):
        return x + y



#
# s1 = StatMethod(2)
# s1.method3()
# s1.method1()
# StatMethod.method2()

print(StatMethod.method3(8, 4))