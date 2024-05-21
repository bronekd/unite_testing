class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def simplify(self):
        gcd = self.find_gcd(self.numerator, self.denominator)
        self.numerator //= gcd
        self.denominator //= gcd

    @staticmethod
    def find_gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    def __add__(self, other): # +
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        result = Fraction(new_numerator, new_denominator)
        result.simplify()
        return result

    def __radd__(self, other):  # +=
        return self.__add__(other)

    def __truediv__(self, other): # /
        if other.numerator == 0:
            raise ValueError("Cannot divide by zero")
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        result = Fraction(new_numerator, new_denominator)
        result.simplify()
        return result

    def __rtruediv__(self, other): # /=
        return self.__truediv__(other)

    def copy(self):
        return Fraction(self.numerator, self.denominator)

    def __eq__(self, other): # ==
        a = self.copy()
        b = other.copy()
        a.simplify()
        b.simplify()
        return a.numerator == b.numerator and a.denominator == b.denominator

"""
a = Fraction(2,2)
b = Fraction(2, 2)
c = Fraction(3, 3)

print(a+b)
a += b
print(a==c)
print(a)
"""