'''3.10. Все функции: придумайте информацию, которую можно было бы хранить в 
списке. Например, создайте список гор, рек, стран, городов, языков… словом,
чего угодно. Напишите программу, которая создает список элементов,а затем
вызывает каждую функцию, упоминавшуюся в этой главе, хотя бы один раз.'''

cities = ['cанкт-петербург', 'москва', 'казань', 'воронеж', 'новосибирск',
'самара']

print(f'Я живу в городе {cities[0].title()}')

cities[2] = 'петропавловск-камчатский'
print(f'\n{cities}')

cities.append('казань')
cities.insert(2, 'магнитокорск')
print(f'\n{cities}')

del cities[-2]
print(f'\n{cities}')

popped_city = cities.pop(0)
print(f'\n{cities}')
print(popped_city.upper())

cities.insert(0, popped_city)
print(f'\n{cities}')

removed_city = 'воронеж'
cities.remove(removed_city)
print(f'\n{removed_city.title()} разбомбили, список обновлен.')
print(f'{cities}')


print(f'\n{sorted(cities)}')

cities.sort(reverse=True)
print(f'\n{cities}')

print(f'Всего в списке {len(cities)} городов.')