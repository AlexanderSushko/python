# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия,
# год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

fields = ('Name ', 'Second name ', 'Year of birth ', 'Where do you live ', 'Your email ', 'Your telephone ')
data = []
while True:
    change = input ('Нажмите любую кнопку или q для выхода - ')
    if change == 'q':
        break
    person = {}
    for field in fields:
        person[field] = input(f'Введите значение поля - {field} ')
    data.append(person)
    print(data)