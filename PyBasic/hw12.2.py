class Item:
    def __init__(self, name, price, description, dimensions):
        self.name = name
        self.price = price
        self.description = description
        self.dimensions = dimensions

    def __str__(self):
        return f"{self.name}, price: {self.price}"


class User:
    def __init__(self, name, surname, numberphone):
        self.name = name
        self.surname = surname
        self.numberphone = numberphone

    def __str__(self):
        return f"{self.name} {self.surname}"


class Purchase:
    def __init__(self, user):
        self.products = {}  # Словник для товарів і їх кількості
        self.user = user

    def add_item(self, item, cnt):
        # Додаємо товар до замовлення, або оновлюємо кількість
        if item in self.products:
            self.products[item] += cnt
        else:
            self.products[item] = cnt

    def get_total(self):
        # Обчислення загальної вартості замовлення
        return sum(item.price * cnt for item, cnt in self.products.items())

    def __str__(self):
        # Форматоване виведення інформації про замовлення
        items_str = "\n".join(
            [f"{item.name}: {cnt} pcs." for item, cnt in self.products.items()]
        )
        return f"User: {self.user}\nItems:\n{items_str}"


# Створюємо товари
lemon = Item('lemon', 5, "yellow", "small")
apple = Item('apple', 2, "red", "middle")
print(lemon)  # lemon, price: 5

# Створюємо користувача
buyer = User("Ivan", "Ivanov", "02628162")
print(buyer)  # Ivan Ivanov

# Створюємо замовлення
cart = Purchase(buyer)
cart.add_item(lemon, 4)
cart.add_item(apple, 20)
print(cart)
"""
User: Ivan Ivanov
Items:
lemon: 4 pcs.
apple: 20 pcs.
"""

assert isinstance(cart.user, User) is True, 'Екземпляр класу User'
assert cart.get_total() == 60, "Всього 60"
assert cart.get_total() == 60, 'Повинно залишатися 60!'

# Додаємо товар до замовлення
cart.add_item(apple, 10)
print(cart)
"""
User: Ivan Ivanov
Items:
lemon: 4 pcs.
apple: 30 pcs.
"""

assert cart.get_total() == 80, "Повинно бути 80!"
