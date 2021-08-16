# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
def div(*args):

    try:
        arg1 = int(input("Введите делимое число "))
        arg2 = int(input("Введите делитель "))
        result = arg1 / arg2
    except ValueError:
        return 'Ошибка, число не введено !'
    except ZeroDivisionError:
        return "Деление на ноль невозможно"

    return result

print(f'result  {div()}')