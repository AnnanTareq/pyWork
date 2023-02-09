class Person:

    specis = 'Homo Sapiencs'
    count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.count += 1

    def display(self):
        # print(f'{self.name} is {self.age} years old {self.specis}')
        print(f'{self.name} is {self.age} years old {Person.specis}')


p1 = Person('Karim', 15)
p2 = Person('Anamul', 50)
p3 = Person('Munim', 25)

p1.display()
print(p1.specis)
print(Person.specis)
print(id(Person.specis))
print(id(p1.specis))
print(p1.count)