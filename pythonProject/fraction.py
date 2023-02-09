class Fraction:
    def __init__(self, nr, dr=1):
        self.nr = nr
        self.dr = dr
        if self.dr < 0:
            self.dr *= -1
            self.nr *= -1

    def show(self):
        print(f'{self.nr}/{self.dr}')

f = Fraction(-2,-3)
f.show()
