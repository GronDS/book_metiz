'''8.5. Города: напишите функцию describe_city(), которая получает названия города
и страны. Функция должна выводить простое сообщение (например, «Reykjavik is in
Iceland»). Задайте параметру страны значение по умолчанию. Вызовите свою функцию
для трех разных городов, по крайней мере один из которых не находится в стране по
умолчанию.'''

def describe_city(city, country='France'):
    print(f'{city.title()} is in {country.title()}')

describe_city('paris')
describe_city('moscow', 'russia')
describe_city(city= 'london', country= 'united kingdom')