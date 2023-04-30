"""class Person:
    def __init__(self, name, age):
        self.name = name
        if 20 < age < 80:
            self._age = age
        else:
            raise ValueError('If you want to add age now, then your designated age should between 20 and 80')

    def display(self):
        print('Name = ',self.name,' Age = ',self._age)

    def set_age(self,newAge):
        if 20<newAge<80:
            self._age = newAge
        else:
            raise ValueError('If you want to change the age now, then your designated age should between 20 and 80')


    def get_age(self):
        return self._age


if __name__ == '__main__':
    p = Person('Raj',25)
    p.display()
    p.set_age(p.get_age()+1)
    p.display()

    p1 = Person('Masud',20)
    p1.display()
    p1.set_age(p1.get_age()+5)
    p1.display()
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name, self.age)

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, newAge):
        if 20<newAge<80:
            self._age = newAge
        else:
            raise ValueError('Age should be between 20 and 80')


if __name__ == '__main__':
    p = Person('Tareq',24)
    # print(p.age)
    # p.age = 66
    # print(p.age)
    # p.display()
    # p.age = 78

    p1 = Person('Dany', 25)
    p1.age = 23
    p1.age = p1.age+1
    p1.display()
    p1.age = 65
    p1.display()
    p1.age += 5
    p1.display()


