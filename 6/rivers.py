'''6.5. Реки: создайте словарь с названиями трех больших рек и стран,
по которым протекает каждая река. Одна из возможных пар 
«ключ-значение» — 'nile': 'egypt'.
• Используйте цикл для вывода сообщения с упоминанием 
реки и страны — например, «The Nile runs through Egypt».
• Используйте цикл для вывода названия каждой реки, включенной в словарь.
• Используйте цикл для вывода названия каждой страны, включенной в словарь.'''

rivers = {
    'nile' : 'egypt',
    'amazon' : 'peru',
    'yangtze' : 'china',
    }

for river, country in rivers.items():
    print(f'The {river.title()} runs through {country.title()}')

print('\nThe dict includes rivers:')
for rivers_key in rivers:
    print(rivers_key.title())

print('\nThe dict includes countries:')
for rivers_value in rivers.values():
    print(rivers_value.title())