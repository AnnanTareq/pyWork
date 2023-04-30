from employee import Employee
from datetime import datetime


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print('I am', self.name, self.age, 'years old')

    @classmethod
    def from_str(cls, s):
        name, age = s.split(',')
        return cls(name, int(age))

    @classmethod
    def from_dct(cls, dct):
        return cls(dct['name'], dct['age'])

    @classmethod
    def from_employee(cls, emp):
        name = emp.first_name + ' ' + emp.last_name
        age = datetime.today().year - emp.birth_year
        return cls(name, age)


# p1 = Person('Jony', 20)
# p2 = Person('Jakir', 21)

s = 'Sojib, 23'
p3 = Person.from_str(s)
p3.display()

dct = {'name': 'Mamun', 'age': 22}
p4 = Person.from_dct(dct)
p4.display()

e1 = Employee('Abu jayed', 'Rahi', 1990, 6000)
p5 = Person.from_employee(e1)
p5.display()




"""class Person:
    species = 'Homo Sapiens'
    count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.count += 1

    def display(self):
        print(f'{self.name} is {self.age} years old')


    @classmethod
    def showCount(cls):
        print(f'There are {cls.count} {cls.species}')


Person.showCount()

p1 = Person('John', 20)
p2 = Person('Jack', 34)

Person.showCount()      #it is more natural
#p1.showCount()"""
