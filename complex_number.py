import cmath


class complex_number(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
    def real(self):
        real = self.real
        return complex_number(real, 0)
    def conjugate(x):
        x = str(x)
        x = list(x)
        for i in range(len(x)):
            if x[i] == '+':
                x[i] = '-'
        return "".join(x)



    def imag(self):
        imag = self.imaginary
        return complex_number(0, imag)

    def __add__(self, no):
        real = self.real + no.real
        imaginary = self.imaginary + no.imaginary
        return complex_number(real, imaginary)

    def __sub__(self, no):
        real = self.real - no.real
        imaginary = self.imaginary - no.imaginary
        return complex_number(real, imaginary)

    def __mul__(self, no):
        real = self.real * no.real - self.imaginary * no.imaginary
        imaginary = self.real * no.imaginary + self.imaginary * no.real
        return complex_number(real, imaginary)

    def __truediv__(self, no):
        x = float(no.real ** 2 + no.imaginary ** 2)
        y = self * complex_number(no.real, -no.imaginary)
        real = y.real / x
        imaginary = y.imaginary / x
        return complex_number(real, imaginary)

    def mod(self):
        real = (self.real ** 2 + self.imaginary ** 2) ** 0.5
        return complex_number(real, 0)

    def argument(z):
        x  =float(str(complex_number.real(z)))
        imag =str(complex_number.imag(z))
        y = float(str(imag.split('i')[0]))
        return cmath.phase(complex(x, y))

    def __repr__(self):
        if self.imaginary == 0:
            result = "%.2f" % (self.real)
        elif self.real == 0:
            result = "%.2fi" % (self.imaginary)
        elif self.imaginary > 0:
            result = "%.2f + %.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f - %.2fi" % (self.real, abs(self.imaginary))
        return result




C = map(float, input().split())
D = map(float, input().split())
x = complex_number(*C)
y = complex_number(*D)
final = [x+y, x-y, x*y, x/y, x.mod(), y.mod()]
print('add, sub, mul, div, abs, abs')
print('\n'.join(map(str, final)))
print('real',complex_number.real(x))
print('real',complex_number.real(y))
print('imaginary',complex_number.imag(x))
print('imaginary',complex_number.imag(y))
print('argument',complex_number.argument(y))
print('argument',complex_number.argument(x))
print('conjugate',complex_number.conjugate(x))