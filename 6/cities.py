'''6.11. Города: создайте словарь с именем cities. Используйте 
названия трех городов в качестве ключей словаря. Создайте словарь с 
информацией о каждом городе; включите в него страну, в которой расположен
город, примерную численность населения и один примечательный факт,
относящийся к этому городу. Ключи словаря каждого города должны называться
country, population и fact. Выведите название каждого города и всю
сохраненную информацию о нем.'''

cities = {
    'new york':{
        'country': 'usa',
        'population': 8_804_190,
        'fact' : 'The First Pizzeria In The USA Opened In New York City',
        },
    'paris': {
        'country': 'france',
        'population': 2_165_423,
        'fact' : 'First “Bloody Mary” was made in Paris',
        },
    'moscow': {
        'country': 'russia',
        'population': 12_506_468,
        'fact' : 'Moscow is home to the 200-tonne Tsar Bell, the largest bell in the world',
        },
    }

for city, infolist in cities.items():
    print(f'\nCity : {city.title()}')
    for infoname, info in infolist.items():
        if infoname == 'country':
            if info == 'usa':
                print(f'{infoname.title()} : {info.upper()}')
            else:
                print(f'{infoname.title()} : {info.title()}')
        else:
            print(f'{infoname.title()} : {info}')