'''7.5. Билеты в кино: кинотеатр установил несколько вариантов цены на билеты 
в зависимости от возраста посетителя. Для посетителей младше 3 лет билет 
бесплатный; в возрасте от 3 до 12 билет стоит $10; наконец, если возраст
посетителя больше 12, билет стоит $15. Напишите цикл, который предлагает 
пользователю ввести возраст и выводит цену билета.'''

message = 'Enter your age: '

while True:
    age = int(input(f'{message}'))
    if age < 3:
        print('Your ticket is free.\n')
    if age >= 3 and age <= 12:
        print('Your ticket costs 10$\n')
    if age >12:
        print('Your ticket costs 15$\n')