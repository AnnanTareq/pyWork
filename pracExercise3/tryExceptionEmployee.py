class Employee:
    allowed_domains = {'yahoo.com', 'gmail.com', 'outlook.com'}

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def display(self):
        print(self.name, self.email)

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, new_email):
        domain = new_email[new_email.index('@')+1 : ]
        if domain in Employee.allowed_domains:
            self._email = new_email
        else:
            raise RuntimeError(f'Domain {domain} is not allowed')


e1 = Employee('Jony', 'jony@gmail.com')
e2 = Employee('Jakir', 'jakir@gmail.com')
e3 = Employee('Mamum', 'mamun@yahoo.com')
e4 = Employee('Sumon', 'sumon@gmail.com')
e5 = Employee('Jahid', 'jahid@gmailone.com')
e6 = Employee('Malek', 'malek@outlook.com')
e7 = Employee('Ibrahim', 'ibrahim@aiub.edu')

