'''3.4. Список гостей: если бы вы могли пригласить кого угодно (из живых 
или умерших) на обед, то кого бы вы пригласили? Создайте список,
включающий минимум трех людей, которых вам хотелось бы пригласить на обед.
Затем используйте этот список для вывода пригласительного сообщения каждому
участнику.'''

guests = ['Петр Сергеевич', 'Семен Петрович', 'Алексей Семенович', 
'Мартин Алексеевич', 'Степан Степанович']

for i in range(len(guests)):
    print(f'Дорогой {guests[i].title()}, приглашаю Вас на обед в ресторан западной кухни "McDonald\'s", сегодня в 16:54. С уважением, Gron_D_S.')

'''3.9. Количество гостей: в одной из программ из упражнений с 3.4 по 3.7
используйте len() для вывода сообщения с количеством людей, приглашенных на 
обед.'''

print(f'\nНа обед приглашено {len(guests)} человек.')