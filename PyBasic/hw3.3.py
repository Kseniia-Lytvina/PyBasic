# Примеры списков
example1 = [1, 2, 3, 4, 5, 6]
example2 = [1, 2, 3]
example3 = [1, 2, 3, 4, 5]
example4 = [1]
example5 = []

# Пример 1
if len(example1) == 0:
    result1 = [[], []]
else:
    middle1 = (len(example1) + 1) // 2
    result1 = [example1[:middle1], example1[middle1:]]
print(example1,"=>",result1)

# Пример 2
if len(example2) == 0:
    result2 = [[], []]
else:
    middle2 = (len(example2) + 1) // 2
    result2 = [example2[:middle2], example2[middle2:]]
print(example2,"=>",result2)

# Пример 3
if len(example3) == 0:
    result3 = [[], []]
else:
    middle3 = (len(example3) + 1) // 2
    result3 = [example3[:middle3], example3[middle3:]]
print(example3,"=>",result3)

# Пример 4
if len(example4) == 0:
    result4 = [[], []]
else:
    middle4 = (len(example4) + 1) // 2
    result4 = [example4[:middle4], example4[middle4:]]
print(example4,"=>",result4)

# Пример 5
if len(example5) == 0:
    result5 = [[], []]
else:
    middle5 = (len(example5) + 1) // 2
    result5 = [example5[:middle5], example5[middle5:]]
print(example5,"=>",result5)
