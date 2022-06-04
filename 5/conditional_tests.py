'''5.1. Проверка условий: напишите последовательность условий. 
Выведите описание каждой проверки и ваш прогноз относительно ее результата.
Код должен выглядеть примерно так:
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
• Внимательно просмотрите результаты. Убедитесь в том, что вы понимаете,
почему результат каждой строки равен True или False.
• Создайте как минимум 10 условий. Не менее пяти одних должны давать
результат True, а не менее пяти других —  результат False.'''

food = 'potato'
print('Is food == "potato"? I predict True.')
print(food == 'potato')

print("\nIs food == 'tomato'? I predict False.")
print(food == 'tomato')


animal = 'dog'
print('\nIs animal == "dog"? I predict True.')
print(animal == 'dog')

print("\nIs animal == 'cat'? I predict False.")
print(animal == 'cat')


color = 'red'
print('\nIs color == "red"? I predict True.')
print(color == 'red')

print("\nIs color == 'blue'? I predict False.")
print(color == 'blue')


quality = 1080
print('\nIs quality == 1080? I predict True.')
print(quality == 1080)

print("\nIs quality == 360? I predict False.")
print(quality == 360)


name = 'John'
print('\nIs name == "John"? I predict True.')
print(name == 'John')

print("\nIs name == 'Tom'? I predict False.")
print(name == 'Tom')

'''5.2. Больше условий: количество условий не ограничивается десятью.
Попробуйте написать другие условия и включить их в conditional_tests.py.
Программа должна выдавать по крайней мере один истинный и один ложный
результат для следующих видов проверок:
• Проверка равенства и неравенства строк.
• Проверки с использованием функции lower().
• Числовые проверки равенства и неравенства, условий «больше», 
«меньше», «больше или равно», «меньше или равно».
• Проверки с ключевым словом and и or.
• Проверка вхождения элемента в список.
• Проверка отсутствия элемента в списке.'''

print(f'name = \'John\' is {name == "John"}')
print(f'name != \'Tom\' is {name != "Tom"}')

print(f'lowername = \'john\' is {name.lower() == "john"}')
print(f'lowername = \'JoHn\' is {name.lower() == "JoHn"}')

print(f'\nquality = 1080 is {quality == 1080}')
print(f'quality = 180 is {quality == 180}')
print(f'quality != 180 is {quality != 180}')
print(f'quality > 180 is {quality > 180}')
print(f'quality < 18000 is {quality < 18_000}')

test1 = animal == "dog" and color == "red"
print(f'\nanimal = \'dog\' and color = \'red\' is {test1}')

test2 = animal == "dog" or color == "blue"
print(f'animal = \'dog\' or color = \'blue\' is {test2}')

test3 = animal == "cat" or color == "blue"
print(f'animal = \'cat\' or color = \'blue\' is {test3}')

all_vars = [food, animal, color, quality, name]
print(f'\nanimal in vars is {animal in all_vars}')
print(f'dog in vars is {"dog" in all_vars}')

print(f'Monica in vars is {"Monica" in all_vars}')