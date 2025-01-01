class Rectangle:
    def __init__(self, width, height):
        """Ініціалізація прямокутника з шириною та висотою."""
        self.width = width
        self.height = height

    def get_square(self):
        """Обчислює площу прямокутника."""
        return self.width * self.height

    def __eq__(self, other):
        """Порівнює два прямокутники за площею."""
        if isinstance(other, Rectangle):
            return self.get_square() == other.get_square()
        return False

    def __add__(self, other):
        """Складає площі двох прямокутників і створює новий прямокутник."""
        if isinstance(other, Rectangle):
            new_area = self.get_square() + other.get_square()
            # Створення нового прямокутника
            new_width = 1
            new_height = new_area // new_width
            while new_width * new_height != new_area:
                new_width += 1
                new_height = new_area // new_width
            return Rectangle(new_width, new_height)
        raise ValueError("Складати можна тільки з іншими прямокутниками.")

    def __mul__(self, n):
        """Множить площу прямокутника на число і створює новий прямокутник."""
        if isinstance(n, (int, float)) and n > 0:
            new_area = self.get_square() * n
            # Створення нового прямокутника
            new_width = 1
            new_height = new_area // new_width
            while new_width * new_height != new_area:
                new_width += 1
                new_height = new_area // new_width
            return Rectangle(new_width, new_height)
        raise ValueError("Множити можна тільки на додатнє число.")

    def __str__(self):
        """Повертає строкове представлення прямокутника."""
        return f"Rectangle({self.width}, {self.height}), Area: {self.get_square()}"


# Тестування
r1 = Rectangle(2, 4)
r2 = Rectangle(3, 6)

# Test1
assert r1.get_square() == 8, "Test1 failed"
# Test2
assert r2.get_square() == 18, "Test2 failed"

# Test3: Складання прямокутників
r3 = r1 + r2
assert r3.get_square() == 26, "Test3 failed"

# Test4: Множення прямокутника на число
r4 = r1 * 4
assert r4.get_square() == 32, "Test4 failed"

# Test5: Порівняння прямокутників за площею
assert Rectangle(3, 6) == Rectangle(2, 9), "Test5 failed"


print(r1)  # Rectangle(2, 4), Area: 8
print(r2)  # Rectangle(3, 6), Area: 18
print(r3)  # Rectangle(13, 2), Area: 26
print(r4)  # Rectangle(16, 2), Area: 32

