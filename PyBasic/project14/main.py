from student import Student
from group import Group, GroupLimitException

# Створення студентів
st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')

# Створення групи
gr = Group('PD1')

# Додавання студентів
gr.add_student(st1)
gr.add_student(st2)

# Виведення групи
print(gr)

# Перевірки
assert gr.find_student('Jobs') == st1  # 'Steve Jobs'
assert gr.find_student('Jobs2') is None

# Видалення студента
gr.delete_student('Taylor')
print(gr)  # Only one student

# Перевірка перевищення ліміту
try:
    for i in range(9):  # Додаємо ще 9 студентів
        gr.add_student(Student('Male', 20 + i, f'Student{i}', f'Lastname{i}', f'RB{i}'))
    # Додаємо 11-го студента
    gr.add_student(Student('Female', 22, 'Extra', 'Student', 'RB11'))
except GroupLimitException as e:
    print(f"Помилка при додаванні: {e}")
