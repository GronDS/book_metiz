'''4.1. Пицца: вспомните по крайней мере три названия ваших любимых видов пиццы.
Сохраните их в списке и используйте цикл for для вывода всех названий. #4.1.1
• Измените цикл for так, чтобы вместо простого названия пиццы выводилось 
сообщение, включающее это название. Таким образом, для каждого элемента 
должна выводиться строка с простым текстом, например:
«I like pepperoni pizza».
• Добавьте в конец программы (после цикла for) строку с завершающим 
сообщением. Таким образом, вывод должен состоять из трех (и более) строк 
с названиями пиццы и дополнительного 
сообщения — скажем, «I really love pizza!»'''

pizzas = ['Margherita', 'marinara', 'hawaiian']

for pizza in pizzas:
    # print(pizza) #4.1.1
    print(f'I like {pizza} pizza')
print('\nI really love pizza!')

'''4.11. Моя пицца, твоя пицца: начните с программы из упражнения 4.1.
Создайте копию списка с видами пиццы, присвойте ему имя friend_pizzas.
Затем сделайте следующее:
• Добавьте новую пиццу в исходный список.
• Добавьте другую пиццу в список friend_pizzas.
• Докажите, что в программе существуют два разных списка.
Выведите сообщение «My favorite pizzas are:»,
а затем первый список в цикле for. Выведите сообщение
«My friend's favorite pizzas are:», а затем второй список в цикле for.
Убедитесь в том, что каждая новая пицца находится в соответствующем списке.'''

friend_pizzas = pizzas[:]

friend_pizzas.append('four cheese')
pizzas.append('pepperoni')

print('\nMy favorite pizzas are:')
for pizza in pizzas:
    print(pizza)

print('\nMy friend\'s favorite pizzas are:')
for friend_pizza in friend_pizzas:
    print(friend_pizza)