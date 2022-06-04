'''6.8. Домашние животные: создайте несколько словарей, имена которых 
представляют клички домашних животных. В каждом словаре сохраните информацию 
о виде животного и имени владельца. Сохраните словари в списке с именем pets.
Переберите элементы списка.
В процессе перебора выведите всю имеющуюся информацию о каждом животном'''

bobby = {
    'name' : 'bobby',
    'type' : 'dog',
    'owner' : 'billy',
    }

chappy = {
    'name' : 'chappy',
    'type' : 'frog',
    'owner' : 'james',
    }

kotty = {
    'name' : 'kotty',
    'type' : 'cat',
    'owner' : 'ann',
    }

pets = [bobby, chappy, kotty]

for pet in pets:
    print(f'{pet["name"].title()} is a {pet["type"]}, its owner is {pet["owner"].title()}\n')