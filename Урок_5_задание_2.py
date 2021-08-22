# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

my_file = open('my_file2.txt', 'r')
file_data = my_file.read()
print(f'Данные из файла: \n {file_data}')
my_file = open('my_file2.txt', 'r')
file_data = my_file.readlines()
print(f'В файле строк : {len(file_data)}')
my_file = open('my_file2.txt', 'r')
file_data = my_file.readlines()
for i in range(len(file_data)):
    print(f'Окличество символов {i + 1} - ой строки {len(file_data[i])}')
my_file = open('my_file2.txt', 'r')
file_data = my_file.read()
file_data = file_data.split()
print(f'Количество слов - {len(file_data)}')
my_file.close()