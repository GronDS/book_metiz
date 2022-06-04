'''5.7. Любимый фрукт: составьте список своих любимых фруктов. 
Напишите серию независимых команд if для проверки того,
присутствуют ли некоторые фрукты в списке.
• Создайте список трех своих любимых фруктов и назовите его favorite_fruits.
• Напишите пять команд if. Каждая команда должна проверять, 
входит ли определенный тип фрукта в список. Если фрукт входит в список,
блок if должен выводить сообщение вида «You really like bananas!».'''

favorire_fruits = ('bananas', 'orange', 'pineapple')
fruits = ['apple', 'orange', 'pineapple', 'bananas', 'pear']

for fruit in fruits:
    if fruit in favorire_fruits:
        print(f'You really like {fruit}!')