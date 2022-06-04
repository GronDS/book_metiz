'''7.6. Три выхода: напишите альтернативную версию упражнения 7.4 или упражнения
7.5, в которой каждый пункт следующего списка встречается хотя бы один раз:
• Завершение цикла по проверке условия в команде while.
• Управление продолжительностью выполнения цикла в зависимости от переменной
active
• Выход из цикла по команде break, если пользователь вводит значение 'quit'.'''

message = 'Enter your age(or "quit"): '
active = 0
age = 0
while int(age) < 100:
    age = (input(f'{message}'))
    if age == 'quit':
        break
    if int(age) < 3:
        print('Your ticket is free.\n')
    if int(age) >= 3 and int(age) <= 12:
        print('Your ticket costs 10$\n')
    if int(age) >12:
        print('Your ticket costs 15$\n')
    if active >= 10:
        break
    active += 1