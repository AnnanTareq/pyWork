class Person:
    def greet(self):
        print('I am a Person')


class Teacher(Person):
    def greet(self):
        Person.greet(self)
        print('I am a Teacher')


class Student(Person):
    def greet(self):
        Person.greet(self)
        print('I am a student')


class TeachingAssistant(Student, Teacher):
    def greet(self):
        super().greet()
        print('I am teaching assistant')


x = TeachingAssistant()
x.greet()