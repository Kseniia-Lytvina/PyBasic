import random

lst_length = random.randint(3, 10)
lst = []

for i in range(lst_length):
    lst += [random.randint(1, 100)]

new_lst = [lst[0], lst[2], lst[-2]]
print(lst, "=>", new_lst)