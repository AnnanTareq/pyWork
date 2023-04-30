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

    def __str__(self):
        return f'{self.nr}/{self.dr}'

    def __repr__(self):
        return f'{self.nr}/{self.dr}'

    def __add__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        f = Fraction(self.nr * other.dr + other.nr * self.dr, self.dr * other.dr)
        f._reduce()
        return f

    def __radd__(self, other):
        return self.__add__(other)

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

    def __eq__(self, other):
        return (self.nr * other.dr) == (self.dr * other.nr)

    def __lt__(self, other):                #less than
        return (self.nr * other.dr) < (self.dr * other.nr)

    def __le__(self, other):
        return (self.nr * other.dr) <= (self.dr * other.nr)

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


f1 = Fraction(22, 23)
#f1.show()
f2 = Fraction(22, 23)
#f2.show()
f3 = Fraction(2, 3)
# print(f1 == f2)
# print(f1 != f3)
# print(f1 < f3)
# print(f1 <= f3)
# print(f1 <= f2)
# print(str(f1))
# print(f1)
#
# L = [f1, f2, f3]        #use __repr__ method
#
# print(L)

f4 = f1 + 5
print(f4)

f5 = 5 + f1
print(f5)
