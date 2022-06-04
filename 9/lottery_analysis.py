'''9.15. Анализ лотереи: напишите цикл, который проверяет,
насколько сложно выиграть в смоделированной вами лотерее. Создайте список или
кортеж с именем my_ticket. Напишите цикл, который продолжает генерировать 
комбинации до тех пор, пока не выпадет выигрышная комбинация. Выведите 
сообщение с информацией о том, сколько выполнений цикла понадобилось для 
получения выигрышной комбинации.'''

from random import choices

keys = ('A', 'B', 'C', 'D', 'E', 1, 2, 3, 4, 5, 6, 7, 8, 9, 0)

winner_ticket = choices(population= keys, k= 4)
print(f'Winner combination: {winner_ticket}')

my_ticket = []
counter = 0
 
 
while True:
    my_ticket = choices(population= keys, k= 4)
    if set(my_ticket) != set(winner_ticket):
        counter += 1
    else :
        print(f'You win with the ticket {my_ticket}.\
            \nYou tried {counter} times!')
        break