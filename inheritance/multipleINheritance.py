class Person:
    def greet(self):
        print('I am a Person')


class Teacher(Person):
    def greet(self):
        super().greet()
        print('I am a teacher')


class Student(Person):
    def greet(self):
        super().greet()
        print('I am a student')


class TeachingAssistant(Student, Teacher):
    def greet(self):            #If here is not function available then go to student class and print
        super().greet()

        print('I am a teaching assistant')


x = TeachingAssistant()
x.greet()
print('Student')
s = Student()
s.greet()
