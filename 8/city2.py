'''8.6. Названия городов: напишите функцию city_country(), которая получает
название города и страну. Функция должна возвращать строку в формате 
"Santiago, Chile". Вызовите свою функцию по крайней мере для трех пар
«город —  страна» и выведите возвращенное значение.'''

def city_country(city, country):
    return (f'{city.title()}, {country.title()}')

city = city_country('santiago', 'chille')
print(city)

city = city_country('paris', 'france')
print(city)

city = city_country('kyiv', 'ukraine')
print(city)