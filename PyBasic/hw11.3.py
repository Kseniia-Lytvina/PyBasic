def is_even(number):
    """Перевірка парності числа без використання операцій ділення."""
    binary_representation = bin(number)
    return binary_representation[-1] == '0'

assert is_even(2494563894038**2) == True, 'Test1'
assert is_even(1056897**2) == False, 'Test2'
assert is_even(24945638940387**3) == False, 'Test3'

print("OK")
