# Python class to add 2 numbers manually using OOPS concept


class Complex:
    def __init__(self, real, imag):
        self.real=real
        self.imag=imag

    def add(self,number):
        real = self.real + number.real
        imag = self.imag + number.imag
        result = Complex(real,imag)
        return result


n1 = Complex(1,6)
n2 = Complex(2,7)

result = n1.add(n2)
# here self will be n1 and 'number' is n2

print('real=',result.real)
print('imag=',result.imag)