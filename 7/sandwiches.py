'''7.8. Сэндвичи: создайте список с именем sandwich_orders, заполните его 
названиями различных видов сэндвичей. Создайте пустой список с именем 
finished_sandwiches. В цикле переберите элементы первого списка и выведите
сообщение для каждого элемента (например, «I made your tuna sandwich»).
После этого каждый сэндвич из первого списка перемещается в список 
finished_sandwiches. После того как все элементы первого списка будут
обработаны, выведите сообщение с перечислением всех изготовленных сэндвичей.'''

sandwich_orders = ['chicken sandwich', 'egg sandwich', 'seafood sandwich',
'roast beef sandwich', 'grilled cheese']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f'I made your {sandwich.title()}')
    finished_sandwiches.append(sandwich.title())
print(f'List of cooked sandwiches: {finished_sandwiches}')