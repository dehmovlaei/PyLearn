class Fraction:
    def __init__(self, num, den):
        self.numerator = num
        self.denominator = den
    
    def sum(self, f1, f2):
        result_num = f1.numerator * f2.denominator + f1.denominator * f2.numerator
        result_den = f1.denominator * f2.denominator
        x = Fraction(result_num, result_den)
        return x
    
    def sub(self, f1, f2):
        result_num = f1.numerator * f2.denominator - f1.denominator * f2.numerator
        result_den = f1.denominator * f2.denominator
        x = Fraction(result_num, result_den)
        return x
    
    def mul(self, f1, f2):
        result_num = f1.numerator * f2.numerator
        result_den = f1.denominator * f2.denominator
        x = Fraction(result_num, result_den)
        return x
    
    def div(self, f1, f2):
        result_num = f1.numerator * f2.denominator
        result_den = f1.denominator * f2.numerator
        x = Fraction(result_num, result_den)
        return x

    def fraction_to_number(self):
        result = self.numerator / self.denominator
        return result
    
    def simplifying(self):
        gcd = 1
        for i in range(2, self.numerator+1):
            if self.numerator % i == 0 and self.denominator % i == 0:
                if i > gcd:
                    gcd = i
        x = Fraction(self.numerator/gcd, self.denominator/gcd)
        return x

    def show(self):
        print(self.numerator, '/', self.denominator)

a = Fraction(12, 36)
a.show()

b = Fraction(17, 12)
b.show()

z = a.sum(a, b)
z.show()

z = a.sub(a, b)
z.show()

z = a.mul(a, b)
z.show()

z = a.div(a, b)
z.show()

z = a.fraction_to_number()
print(z)

z = a.simplifying()
z.show()