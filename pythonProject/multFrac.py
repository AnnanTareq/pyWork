class Fraction:
    def __init__(self, nr, dr=1):
        self.nr = nr
        self.dr = dr
        if self.dr < 0:
            self.dr *= -1
            self.nr *= -1

    def multiply(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        return Fraction(self.nr * other.nr, self.dr * other.dr)

    def add(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        return Fraction(self.nr * other.dr + other.nr * self.dr, self.dr * other.dr)

    def show(self):
        print(f'{self.nr}/{self.dr}')

f = Fraction(2,3)
f.show()
f1 = Fraction(3,4)
f1.show()
f3 = f.multiply(f1)
f3.show()
f3 = f.add(f1)
f3.show()
f3 = f.add(5)
f3.show()
f3 = f.multiply(5)
f3.show()