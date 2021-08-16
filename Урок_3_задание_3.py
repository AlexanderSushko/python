# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму
# наибольших двух аргументов.

def function(number1 , number2, number3):
    if number1 >= number3 and number2 >= number3:
        return number1 + number2
    elif number1 > number2 and number1 < number3:
        return number1 + number3
    else:
        return number2 + number3

print(f'Результат - {function(int(input("Первое число ")), int(input("Второе число ")), int(input("Третье число ")))}')