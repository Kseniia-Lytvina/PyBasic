class GroupLimitException(Exception):
    """Користувацький виняток для перевищення ліміту студентів у групі."""
    def __init__(self, message="Група не може містити більше 10 студентів."):
        super().__init__(message)


class Human:
    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.age} years old, {self.gender}"


class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"{super().__str__()}, Record Book: {self.record_book}"


class Group:
    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        """Додає студента до групи. Якщо кількість студентів перевищує 10, викликає виняток."""
        if len(self.group) >= 10:
            raise GroupLimitException()
        self.group.add(student)

    def delete_student(self, last_name):
        """Видаляє студента за прізвищем."""
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def find_student(self, last_name):
        """Шукає студента за прізвищем."""
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = "\n".join(str(student) for student in self.group)
        return f"Group: {self.number}\nStudents:\n{all_students}"


st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')

gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)

try:
    for i in range(9):
        student = Student('Male', 20 + i, f'Student{i+1}', f'Lastname{i+1}', f'RB{i+1}')
        gr.add_student(student)
except GroupLimitException as e:
    print(f"Помилка: {e}")

print(gr)

try:
    extra_student = Student('Female', 22, 'Extra', 'Student', 'RB999')
    gr.add_student(extra_student)
except GroupLimitException as e:
    print(f"Помилка при додаванні: {e}")
