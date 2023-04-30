class Product:
    def __init__(self):
        self.data1 = 10
        # self._data2 = 20
        self.__data2 = 20

    def method1(self):
        print('Method1')
    #
    # def _method2(self): # Can access directly
    #     pass


    def __method2(self): #can not access from outside directly, but can access indirectly
        print('Method2')


p1 = Product()
p1.method1()
print(p1.data1)
# print(p1.__data2)
"""

This is not possible for this method
p1.__method2()
print(p1.data1)
print(p1.__data2)"""

"""
By use of printed method, can access indirectly.

print(dir(p1))

print(p1._Product__data2)
"""

print(p1._Product__data2)