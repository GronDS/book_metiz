'''6.7. Люди: начните с программы, написанной для упражнения 6.1. 
Создайте два новых словаря, представляющих разных людей, и сохраните все
три словаря в списке с именем people.
Переберите элементы списка людей. 
В процессе перебора выведите всю имеющуюся информацию о каждом человеке.'''

person0 = {
    'first_name' : 'gabe',
    'last_name' : 'newell',
    'age' : '59',
    'birthplace' : 'seattle',
    }

person1 = {
    'first_name' : 'hideo',
    'last_name' : 'kojima',
    'age' : '58',
    'birthplace' : 'tokyo',
    }

person2 = {
    'first_name' : 'satoshi',
    'last_name' : 'tajiri',
    'age' : '56',
    'birthplace' : 'machida',
    }
people = [person0, person1, person2]

for person in people:
    print(f'Fullname: {person["first_name"].title()} {person["last_name"].title()}')
    print(f'\tAge: {person["age"]}')
    print(f'\tBirthplace: {person["birthplace"].title()}\n')