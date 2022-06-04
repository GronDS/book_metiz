'''7.9. Без пастрами: используя список sandwich_orders из упражнения 7.8, 
проследите за тем, чтобы значение 'pastrami' встречалось в списке 
как минимум три раза. Добавьте в начало программы код для вывода сообщения
о том, что пастрами больше нет, и напишите цикл while для удаления 
всех вхождений 'pastrami' из sandwich_orders. Убедитесь в том,
что в finished_sandwiches значение 'pastrami' не встречается ни одного раза.'''

sandwich_orders = ['chicken sandwich', 'pastrami', 'egg sandwich', 'pastrami', 
'seafood sandwich', 'pastrami', 'roast beef sandwich', 'pastrami',
'grilled cheese']
print(sandwich_orders)
print('No more pastrami')

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print([sandwich.title() for sandwich in sandwich_orders])