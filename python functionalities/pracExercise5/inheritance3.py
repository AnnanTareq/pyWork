class Person:
    def __init__(self, id):
        self.id = id


class Teacher(Person):
    def __init__(self, id):
        super().__init__(id)
        self.id += 'T'


class Student(Person):
    def __init__(self, id):
        super().__init__(id)
        self.id += 'S'


class TeachingAssistant(Student, Teacher):
    def __init__(self, id):
        super().__init__(id)
        #Teacher.__init__(self, id)


print('Teaching Assistant ID')
x = TeachingAssistant('2212')
print(x.id)
y = TeachingAssistant('4342')
print(y.id)
z = TeachingAssistant('9893')
print(z.id)

print('\nStudent Id')
s = Student('0001')
print(s.id)
s1 = Student('0002')
print(s1.id)

print('\nTeacher ID')
t1 = Teacher('1234')
print(t1.id)

print('\nPerson Id')
p1 = Person('5678')
print(p1.id)
p2 = Person('5677')
print(p2.id)