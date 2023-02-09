"""Type : 1"""
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, new_value):
        if new_value > 0:
            self._radius = new_value
        else:
            raise ValueError('Value can not be a negative')

    @property
    def area(self):
        return 3.14 * self._radius * self._radius

    @property
    def circumference(self):
        return 2 * 3.14 * self._radius

    @property
    def diameter(self):
        return 2 * self._radius


c1 = Circle(2)

print(c1.area)
print(c1.circumference)
print(c1.diameter)




"""
Type 2:

class Circle:
    def __init__(self, radius):
        if radius < 0:
            raise ValueError('Value can not be a negative number')
        else:
            self.__radius = radius

    @property
    def area(self):
        return self.__radius * self.__radius * 3.14


    @area.setter
    def area(self, new):
        if new > 0:
            self.__radius = new
            return 3.14 * self.__radius * self.__radius
        else:
            raise ValueError('Value should not be a negative number')

    @property
    def circumference(self):
        return self.__radius

    @circumference.setter
    def circumference(self, new_val):
        if new_val > 0:
            self.__radius = new_val
            return 2 * 3.14 * self.__radius
        else:
            raise ValueError('Radius Can not be a negative number')

    @property
    def diameter(self):
        return self.__radius * 2

    @diameter.setter
    def diameter(self, new_value):
        if new_value > 0:
            self.__radius = new_value
            return 2 * self.__radius
        else:
            raise ValueError('Values can not be negative number')


c1 = Circle(5)
print(c1.area)
print(c1.diameter)
print(c1.circumference)

# c1.area = -1              #It will give a value error 
# print(c1.area)
"""