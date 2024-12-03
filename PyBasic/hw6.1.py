import string

input_data = input("Введіть дві літери через дефіс (наприклад, a-c): ")

start, end = input_data.split('-')
all_letters = string.ascii_letters
start_index = all_letters.index(start)
end_index = all_letters.index(end)
result = all_letters[start_index:end_index + 1]

print(result)
