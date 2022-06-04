'''6.1. Человек: используйте словарь для сохранения информации об 
известном вам человеке. Сохраните имя, фамилию, возраст и город, 
в котором живет этот человек. Словарь должен содержать ключи с такими 
именами, как first_name, last_name, age и city. Выведите
каждый фрагмент информации, хранящийся в словаре.'''

person = {
    'first_name' : 'gabe',
    'last_name' : 'newell',
    'age' : '59',
    'city' : 'seattle',
    }

print(f"Name : {person['first_name'].title()} {person['last_name'].title()}")
print(f'Age : {person["age"]}')
print(f"City : {person['city'].title()} ")