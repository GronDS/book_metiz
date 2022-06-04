'''4.2. Животные: создайте список из трех (и более) животных, обладающих общей 
характеристикой. Используйте цикл for для вывода названий всех животных.
• Измените программу так, чтобы вместо простого названия выводилось 
сообщение, включающее это название, например, «A dog would make a great pet».
• Добавьте в конец программы строку с описанием общего свойства.
Например, можно вывести сообщение
«Any of these animals would make a great pet!».'''

animals = ['wolf', 'lion', 'tiger', 'cat','frog']

for animal in animals:
    # print(animal)
    print(f'A {animal} is a beautiful creature')
print('\nAny of these animals would make a great pet!')

'''4.10. Сегменты: добавьте в конец одной из программ, написанных в этой главе, 
фрагмент, который делает следующее:
• Выводит сообщение «The irst three items in the list are:»,
а затем использует сегмент для вывода первых трех элементов из списка.
• Выводит сообщение «Three items from the middle of the list are:», а затем 
использует сегмент для вывода первых трех элементов из середины списка.
• Выводит сообщение «The last three items in the list are:», 
а затем использует сегмент для вывода последних трех элементов из списка'''

print(f'The first three items in the list are:\n{animals[0:3]}')

middle = animals[(int(len(animals)/2) - 1):(int(len(animals)/2) + 2)]
print(f'\nThree items from the middle of the list are:\n{middle}')

print(f'\nThe last three items in the list are:\n{animals[-3:]}')