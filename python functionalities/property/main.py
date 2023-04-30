class Product:
    def __init__(self,x,y):
        self._x = x
        self._y = y

    def display(self):
        print(self._x, self._y)

    def value(self):
        return self._x

    @property
    def value1(self):
        return self._x

    @value1.setter
    def value1(self, val):
        self._x = val
"""
    
    @property
    def value(self):
        return self._x
    
    @value.setter
    def value(self,val):
        self._x = val
        
        
    without this method, cannot assign any kind of value as a instance variable
     
    p2 = Product(11,22)
    p2.value = 100

p2 = Product(11,22)

print(p2.value())

print(p2.value)

        
        """




p1 = Product(45, 77)

print(p1.value1)
print(p1.value1+16)

p1.value1 = 50
print(p1.value1)
print('addition = ',p1.value1+10)

#
#     @property
#     def value(self):                #getter method
#         return self._x
#
#     @value.setter                   #setter method
#     def value(self,v):              #name should be same as 'value'
#         self._x = v
#
#     @property
#     def new(self):
#         return self._y
#
#     @new.setter
#     def new(self, val):
#         self._y = val
#
# p = Product(12, 23)
# print(p.value)
# p.value = 90
# print(p.value)
#
# print(p.new)
# p.new = 100
# print(p.new)