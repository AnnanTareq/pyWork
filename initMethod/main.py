class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display(self):
        print('Name: ',self.name)
        print('Age: ',self.age)

    def greet(self):
        if self.age <80:
            print('Hello, Uncle')

        else:
            print('Hello, Gradpa')


p1 = Person('Jony',50)
p1.display()
p1.greet()

p2 = Person('Masud',90)
p2.display()
p2.greet()