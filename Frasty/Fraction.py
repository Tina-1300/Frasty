import math

class Fraction:

    def __init__(self, numerator:int, denominator:int):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")
        self.numerator = numerator
        self.denominator = denominator
        self._simplify()
        
    def _simplify(self):
        if self.numerator == 0:
            self.denominator = 1
            return 
        common_divisor = math.gcd(self.numerator, self.denominator)
        self.numerator //= common_divisor
        self.denominator //= common_divisor
        if self.denominator < 0:
            self.numerator = -self.numerator
            self.denominator = -self.denominator

    def __add__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        if not isinstance(other, Fraction):
            return NotImplemented
        num = self.numerator * other.denominator + other.numerator * self.denominator
        den = self.denominator * other.denominator
        return Fraction(num, den)

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        if not isinstance(other, Fraction):
            return NotImplemented
        num = self.numerator * other.denominator - other.numerator * self.denominator
        den = self.denominator * other.denominator
        return Fraction(num, den)

    def __rsub__(self, other):
        return Fraction(other, 1) - self

    def __mul__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        if not isinstance(other, Fraction):
            return NotImplemented
        num = self.numerator * other.numerator
        den = self.denominator * other.denominator
        return Fraction(num, den)

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        if not isinstance(other, Fraction):
            return NotImplemented
        if other.numerator == 0:
            raise ValueError("Division by zero fraction")
        num = self.numerator * other.denominator
        den = self.denominator * other.numerator
        return Fraction(num, den)

    def __rtruediv__(self, other):
        return Fraction(other, 1) / self

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __repr__(self):
        return f"Fraction({self.numerator}, {self.denominator})"

    def __eq__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        return self.numerator == other.numerator and self.denominator == other.denominator

    def __lt__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        if not isinstance(other, Fraction):
            return NotImplemented
        return self.numerator * other.denominator < other.numerator * self.denominator

    def __le__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        if not isinstance(other, Fraction):
            return NotImplemented
        return self.numerator * other.denominator <= other.numerator * self.denominator

    def __gt__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        if not isinstance(other, Fraction):
            return NotImplemented
        return self.numerator * other.denominator > other.numerator * self.denominator

    def __ge__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        if not isinstance(other, Fraction):
            return NotImplemented
        return self.numerator * other.denominator >= other.numerator * self.denominator
