class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
        
    def add(self, number):
        real = self.real + number.real
        imag = self.imag + number.imag
        result = Complex(real, imag)
        return result


n1 = int(input('First real number: \n'))
n2 = int(input('First imaginary number: \n'))
n3 = int(input('Second real number: \n'))
n4 = int(input('Second imaginary number: \n'))
num1 = Complex(n1, n2)
num2 = Complex(n3, n4)
result = num1.add(num2)
print(result.real)
print(result.imag)