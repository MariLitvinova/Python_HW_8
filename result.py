# Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных.

from function import *

try:                       
    file = open(path, 'r')  
except IOError:             
    print('Создан новый справочник -> phone_book.txt ')
    file = open(path, 'w')
finally:                    
    file.close()

actions = {'1': 'список',
           '2': 'запись',
           '3': 'поиск',
           '4': 'изменение',
           '5': 'удаление',
           'q': 'выход'}

action = None
while action != 'q':
    print('Какое действие хотите совершить?', *[f'{i} - {actions[i]}' for i in actions])
    action = input()
    while action not in actions:
        print('Какое действие хотите совершить?', *[f'{i} - {actions[i]}' for i in actions])
        action = input()
        if action not in actions:
            print('Введены неверные данные')
    if action != 'q':
        if action == '1':
            print_records(path)
        elif action == '2':
            input_records(path)
        elif action == '3':
            find_records(path, *find_char())
        elif action == '4':
            change_records(path)
        elif action == '5':
            delete_records(path)