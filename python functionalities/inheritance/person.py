class Person:
    def __init__(self, name, age, address, phone):
        self.name = name
        self.age = age
        self.address = address
        self.phone = phone

    def greet(self):
        print('Hello, I am ', self.name)

    def is_adult(self):
        if self.age > 18:
            return True
        else:
            return False

    def contact_details(self):
        print(self.address, self.phone)


class Employee(Person):

    def __init__(self, name, age, address, phone, salary, office_address, office_phone):
        # self.name = name
        # self.age = age
        # self.address = address
        # self.phone = phone
        #Person.__init__(self, name, age, address, phone)
        super().__init__(name, age, address, phone)
        self.salary = salary
        self.office_address = office_address
        self.office_phone = office_phone

    def calculate_tax(self):
        if self.salary < 5000:
            return 0
        else:
            return self.salary * 0.05

    def contact_details(self):
        super().contact_details()
        print(self.office_address, self.office_phone)


emp = Employee('Jack', 30, '295 Miami, Florida', '93993949', 9000, 'ABC street', '849746739')
emp.greet()
print(emp.name)
print(emp.age)
print(emp.phone)
print(emp.address)
# emp.is_adult()
# print(isinstance(emp, Employee))
# print(isinstance(emp, Person))
# print(issubclass(Employee, Person))
print(emp.calculate_tax())
emp.contact_details()