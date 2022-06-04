'''7.4. Топпинг для пиццы: напишите цикл, который предлагает пользователю 
вводить дополнения для пиццы до тех пор, пока не будет введено значение
'quit'. При вводе каждого дополнения выведите сообщение о том,
что это дополнение включено в заказ.'''

toppings = '\nEnter the topping you want to add.'
toppings += "\nIf you don\'t want more toppings enter 'quit'. "

a = ''
while True:
    a = input(f'{toppings}')
    if a == 'quit':
        break
    else:
        print(f'\n{a} was added to the order')