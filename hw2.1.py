n = int(input("Введіть чотиризначне число: "))

n1 = n // 1000
n2 = (n// 100) % 10
n3 = (n // 10) % 10
n4 = n % 10

print(n1)
print(n2)
print(n3)
print(n4)
