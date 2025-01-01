from math import gcd

class Fraction:
    def __init__(self, a, b):
        if b == 0:
            raise ValueError("Denominator cannot be zero.")
        self.a = a
        self.b = b

    def simplify(self):
        """Скорочує дріб до найпростішого вигляду."""
        common_divisor = gcd(self.a, self.b)
        self.a //= common_divisor
        self.b //= common_divisor

    def __add__(self, other):
        """Додавання дробів."""
        new_numerator = self.a * other.b + other.a * self.b
        new_denominator = self.b * other.b
        result = Fraction(new_numerator, new_denominator)
        result.simplify()
        return result

    def __sub__(self, other):
        """Віднімання дробів."""
        new_numerator = self.a * other.b - other.a * self.b
        new_denominator = self.b * other.b
        result = Fraction(new_numerator, new_denominator)
        result.simplify()
        return result

    def __mul__(self, other):
        """Множення дробів."""
        new_numerator = self.a * other.a
        new_denominator = self.b * other.b
        result = Fraction(new_numerator, new_denominator)
        result.simplify()
        return result

    def __eq__(self, other):
        """Порівняння дробів на рівність."""
        self_simplified = Fraction(self.a, self.b)
        self_simplified.simplify()
        other_simplified = Fraction(other.a, other.b)
        other_simplified.simplify()
        return self_simplified.a == other_simplified.a and self_simplified.b == other_simplified.b

    def __gt__(self, other):
        """Перевірка, чи поточний дріб більший за інший."""
        return self.a * other.b > self.b * other.a

    def __lt__(self, other):
        """Перевірка, чи поточний дріб менший за інший."""
        return self.a * other.b < self.b * other.a

    def __str__(self):
        """Строкове представлення дробу."""
        return f"Fraction: {self.a}, {self.b}"

# Тестування
f_a = Fraction(2, 3)
f_b = Fraction(3, 6)
f_c = f_b + f_a
assert str(f_c) == 'Fraction: 21, 18'

f_d = f_b * f_a
assert str(f_d) == 'Fraction: 6, 18'

f_e = f_a - f_b
assert str(f_e) == 'Fraction: 3, 18'

assert f_d < f_c  # True
assert f_d > f_e  # True
assert f_a != f_b  # True

f_1 = Fraction(2, 4)
f_2 = Fraction(3, 6)
assert f_1 == f_2  # True

print('OK')
