'''7.10. Отпуск мечты: напишите программу, которая опрашивает пользователей,
где бы они хотели провести отпуск. 
Включите блок кода для вывода результатов опроса.'''

vacation = {}
respondent = 'yes'

while respondent == 'yes':
    name = input('Enter your name: ')
    loc = input('Where would you like to spend your vacation? ')
    vacation[name] = loc

    respondent = input('Would you like to let another person respond?(yes/no)')

print('\n --- Poll Results ---\n')

for person, loca in vacation.items():
    print(f'{person.title()} wants to spend his vacation in {loca}')