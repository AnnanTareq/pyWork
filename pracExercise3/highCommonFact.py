class Fraction:
    def __init__(self, nr, dr=1):
        self.nr = nr
        self.dr = dr
        if self.dr < 0:
            self.dr *= -1
            self.nr *= -1

    def show(self):
        print(f'{self.nr}/{self.dr}')


    @staticmethod
    def hcf(x,y):
        x = abs(x)
        y = abs(y)
        smaller = y if x > y else x
        s = smaller
        #print(s)
        while s > 0:
            if x % s == 0 and y % s == 0:
                 break
            s -= 1
           
        return s


f = Fraction(-2, -3)
print(f.hcf(72, 98))