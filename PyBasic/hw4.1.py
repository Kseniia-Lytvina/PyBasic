lst = [0, 1, 0, 12, 3]
# lst = [0]
# lst = [1, 0, 13, 0, 0, 0, 5]
# lst = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
# Создаём два списка: для ненулевых элементов и нулей
non_zero = []
zero = []

for l in lst:
    if l == 0:
        zero.append(l)  # Добавляем нули в список zero
    else:
        non_zero.append(l)  # Добавляем ненулевые элементы в список non_zero

# Объединяем
result = non_zero + zero

print(lst, "=>", result)
