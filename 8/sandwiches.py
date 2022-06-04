'''8.12. Сэндвичи: напишите функцию, которая получает список компонентов
сэндвича. Функция должна иметь один параметр для любого количества значений,
переданных при вызове функции, и выводить описание заказанного сэндвича.
Вызовите функцию три раза с разным количеством аргументов.'''

def sandwiches(*components):
    print('\nYou order a sandwich with:')
    for component in components:
        print(f'- {component}')


sandwiches('chicken', 'pickles', 'cheese', 'mayo')
sandwiches('pepperoni', 'tomato', 'ketchup')
sandwiches('beef', 'bacon', 'cheese', 'ketchup')