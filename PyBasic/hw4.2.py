# lst = [1, 3, 5]
# lst = [6]
# lst = []
lst = [0, 1, 7, 2, 4, 8]
if len(lst) > 0:
    index_sum = 0

    for i in range(len(lst)):
        if i % 2 == 0:
            index_sum += lst[i]

    # Умножаем сумму на последний элемент списка
    result = index_sum * lst[-1]
else:
    result = 0

print(lst, "=>", result)
