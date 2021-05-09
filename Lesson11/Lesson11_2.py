class CustomZeroDivisionError(Exception):
    def __init__(self, txt):
        self.txt = txt


def custom_division(num_1, num_2):
    if num_2 == 0:
        raise CustomZeroDivisionError("Попытка деления на 0")
    return num_1 / num_2


num_1 = float(input("Введите делимое: "))
num_2 = float(input("Введите делитель: "))

try:
    result = custom_division(num_1, num_2)
except CustomZeroDivisionError as error:
    print(error.txt)
else:
    print(f"{num_1} / {num_2} = {result}")
    