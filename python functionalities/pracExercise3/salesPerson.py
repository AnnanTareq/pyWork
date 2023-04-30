class salesPerson:

    total_revenue = 0
    names = []

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.sales_amount = 0
        salesPerson.names.append(name)

    def make_sale(self, money):
        self.sales_amount += money
        salesPerson.total_revenue += money

    def show(self):
        print(self.name, self.age, self.sales_amount)


s1 = salesPerson('Bob', 23)
s2 = salesPerson('Ted', 22)
s3 = salesPerson('Jack', 32)

s1.make_sale(1000)
s1.make_sale(1200)
s1.make_sale(5000)
s2.make_sale(5000)
s2.make_sale(2300)
s3.make_sale(420)
s3.make_sale(500)

s1.show()
s2.show()
s3.show()

print(salesPerson.total_revenue)
print(salesPerson.names)

