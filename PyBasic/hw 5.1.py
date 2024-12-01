import string
import keyword

variable_name = input("Введіть ім'я змінної: ")

if variable_name == "_":  # Якщо це лише одне "_"
    print(True)
elif "__" in variable_name:  # Якщо є два або більше підкреслень підряд
    print(False)
else:
    if variable_name.isidentifier() and variable_name not in keyword.kwlist:
        if variable_name.islower():
            print(True)
        else:
            print(False)
    else:
        print(False)
