# Примеры списков
example1 = [12, 3, 4, 10]
example2 = [1]
example3 = []
example4 = [12, 3, 4, 10, 8]

# Пример 1
if len(example1) > 0:
    result1 = [example1[-1]] + example1[:-1]
else:
    result1=example1
print(example1,"=>",result1)

# # Пример 2
if len(example2) > 0:
    result2 = [example2[-1]] + example2[:-1]
else:
    result2=example2
print(example2,"=>",result2)


# Пример 3
if len(example3) > 0:
    result3 = [example3[-1]] + example3[:-1]
else:
    result3=example3
print(example3,"=>",result3)

# Пример 4
if len(example4) > 0:
    result4 = [example4[-1]] + example4[:-1]
else:
    result4=example4
print(example4,"=>",result4)