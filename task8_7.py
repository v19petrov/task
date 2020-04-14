class Comp_numb(object):
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

class MyComplex(Comp_numb):
    def __mul__(self, other):
        return MyComplex(self.real * other.real - self.imag * other.imag,
                         self.imag * other.real + self.real * other.imag)

    def __add__(self, other):
        self.real = self.real + other.real
        self.imag = self.imag + other.imag
        return MyComplex(self.real, self.imag)

    def __str__(self):
        return '(%g, %g)' % (self.real, self.imag)


u = MyComplex(2, -1)
v = MyComplex(1, 2)

print(u * v)
print(u + v)
