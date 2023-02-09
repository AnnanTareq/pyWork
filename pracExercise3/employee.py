class Employee:
    domains = set()

    def __init__(self, name, email):
        self.name = name
        self.email = email
        domain = email[email.index('@')+1:]
        Employee.domains.add(domain)

    def display(self):
        print(self.name, self.email)


e1 = Employee('Jony', 'jony@gmail.com')
e2 = Employee('Jakir', 'jakir@gmail.com')
e3 = Employee('Mamum', 'mamun@yahoo.com')
e4 = Employee('Sumon', 'sumon@gmail.com')
e5 = Employee('Jahid', 'jahid@gmailone.com')
e6 = Employee('Malek', 'malek@outlook.com')
e7 = Employee('Ibrahim', 'ibrahim@aiub.edu')

print(Employee.domains)