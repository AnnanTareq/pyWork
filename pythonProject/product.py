class Product():
    def __init__(self, id, marked_price, discount):
        self.id = id
        self.marked_price = marked_price
        self._discount = discount

    @property
    def selling_price(self):
        return self.marked_price - self._discount / 100 * self.marked_price

    @property
    def discount(self):
        if self.marked_price > 500:
            return self.marked_price - ((self._discount+2) / 100 * self.marked_price)
        else:
            return self._discount
        
    def display(self):
        print(self.id, self.marked_price, self.discount)


p1 = Product('X879', 400, 6)
p2 = Product('A234', 100, 5)
p3 = Product('B987', 990, 4)
p4 = Product('H456', 800, 6)

p1.display()
print(p1.id, p1.selling_price)
print(p3.id, p3.selling_price)
print(p4.id, p4.selling_price)
print(p4.id, p4.discount)
