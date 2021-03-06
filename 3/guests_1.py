'''3.5. Изменение списка гостей: вы только что узнали, что один из гостей прийти
не сможет, поэтому вам придется разослать новые приглашения. 
Отсутствующего гостя нужно заменить кем-то другим.
• Начните с программы из упражнения 3.4. Добавьте в конец программы команду
print для вывода имени гостя, который прийти не сможет.
• Измените список и замените имя гостя, который прийти не сможет,
именем нового приглашенного.
• Выведите новый набор сообщений с приглашениями — по одному для каждого
участника, входящего в список.'''

guests = ['Петр Сергеевич', 'Семен Петрович', 'Алексей Семенович', 'Мартин Алексеевич', 'Степан Степанович']

missed_guest = guests.pop(2)
print(f'{missed_guest} не смог пойти \n')

guests.insert(2, 'Валерий Альбертович')

for i in range(len(guests)):
    print(f'Дорогой {guests[i].title()}, приглашаю Вас на обед в ресторан западной кухни "McDonald\'s", сегодня в 16:54. С уважением, Gron_D_S.')


'''3.6. Больше гостей: вы решили купить обеденный стол большего размера.
Дополнительные места позволяют пригласить на обед еще трех гостей.
• Начните с программы из упражнения 3.4 или 3.5. Добавьте в конец программы
команду print, которая выводит сообщение о расширении списка гостей.
• Добавьте вызов insert() для добавления одного гостя в начало списка.
• Добавьте вызов insert() для добавления одного гостя в середину списка.
• Добавьте вызов append() для добавления одного гостя в конец списка.
• Выведите новый набор сообщений с приглашениями — по одному для каждого
участника, входящего в список.'''

print('\nСписок гостей был пополнен!\n')

guests.insert(0, 'Федор Степанович')
guests.insert(3, 'Степан Федорович')
guests.append('Федор Федорович')

for i in range(len(guests)):
    print(f'Дорогой {guests[i].title()}, приглашаю Вас на обед в ресторан западной кухни "McDonald\'s", сегодня в 16:54. С уважением, Gron_D_S.')

'''3.7. Сокращение списка гостей: только что выяснилось, что новый обеденный 
стол привезти вовремя не успеют и места хватит только для двух гостей.
• Начните с программы из упражнения 3.6. 
Добавьте команду для вывода сообщения о том, что на обед приглашаются
всего два гостя.
• Используйте метод pop() для последовательного удаления гостей из списка до
тех пор, пока в списке не останутся только два человека. Каждый раз, 
когда из списка удаляется очередное имя, выведите для этого человека 
сообщение о том, что вы сожалеете об отмене приглашения.
Выведите сообщение для каждого из двух человек, остающихся в списке. 
Сообщение должно подтверждать, что более раннее приглашение остается в силе.
• Используйте команду del для удаления двух последних имен, 
чтобы список остался пустым. Выведите список, чтобы убедиться в том, 
что в конце работы программы список действительно не содержит
ни одного элемента.'''

print('\nПо непредвиденным ранее обстоятельствам на обед приглашаются всего два гостя\n')

while len(guests) > 2:
    pop_guest = guests.pop()
    print(f'{pop_guest.title()}, приношу свои глубочайшие извинения за отмену приглашения. Всего Вам наилучшего!')

for i in range(len(guests)):
    print(f'Дорогой {guests[i].title()}, Ваше приглашение остается в силе. С уважением, Gron_D_S.')
del guests[0]
del guests[0]
print(guests)