class Fraction:
    def __init__(self, nr, dr=1):
        self.nr = nr
        self.dr = dr
        if self.dr < 0:
            self.dr *= -1
            self.nr *= -1
        self._reduce()

    def show(self):
        print(f'{self.nr}/{self.dr}')

    def __add__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        f = Fraction(self.nr * other.dr + other.nr * self.dr, self.dr * other.dr)
        f._reduce()
        return f

    def __sub__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        f = Fraction(self.nr * other.dr - other.nr * self.dr, self.dr * other.dr)
        f._reduce()
        return f

    def __mul__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        f = Fraction(self.nr * other.nr, self.dr * other.dr)
        f._reduce()
        return f

    # def add(self, other):
    #     if isinstance(other, int):
    #         other = Fraction(other)
    #     f = Fraction(self.nr * other.dr + other.nr * self.dr, self.dr * other.dr)
    #     f._reduce()
    #     return f

    def _reduce(self):
        h = Fraction.hcf(self.nr, self.dr)
        if h == 0:
            return

        self.nr //= h
        self.dr //= h

    @staticmethod
    def hcf(x, y):
        x = abs(x)
        y = abs(y)
        smaller = y if x > y else x
        s = smaller
        # print(s)
        while s > 0:
            if x % s == 0 and y % s == 0:
                break
            s -= 1

        return s


#print(Fraction.hcf(122, 48))

f1 = Fraction(22, 24)
f1.show()
f2 = Fraction(22, 24)
# f3 = f.multiply(f1)
# f3.show()
# f3 = f.add(f1)
# f3.show()
# f3 = f.add(5)
# f3.show()
# f3 = f.multiply(5)
# f3.show()
#print(Fraction.hcf(122, 44))

# f5 = f + f1
# f6 = f * f1
# f7 = f - f1
# f5.show()
# f6.show()
# f7.show()
#
print(f1 == f2)
print(f1 == f2)
