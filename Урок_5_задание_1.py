# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.
my_file = open('my_file.txt', 'w')
data = input('Введите данные \n')
while data:
    my_file.writelines(data)
    data = input('Введите данные \n')
    if not data:
        break

my_file.close()
my_file = open('my_file.txt', 'r')
file_data = my_file.readlines()
print(file_data)
my_file.close()