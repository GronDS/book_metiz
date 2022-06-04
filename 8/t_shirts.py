'''8.3. Футболка: напишите функцию make_shirt(), которая получает размер 
футболки и текст, который должен быть напечатан на ней.
Функция должна выводить сообщение с размером и текстом.Вызовите функцию с
использованием позиционных аргументов. Вызовите функцию во
второй раз с использованием именованных аргументов.'''

def make_shirt(text, size):
    print(f'You want a t-shirt with text \'{text}\' size {size}')

make_shirt('Python', 'L')
make_shirt(size = 'L', text = 'Python')

'''8.4. Большие футболки: измените функцию make_shirt(), чтобы по умолчанию
футболки имели размер L и на них выводился текст «I love Python».
Создайте футболку с размером L и текстом по умолчанию, а также футболку
любого размера с другим текстом.'''

print('\n-- big t-shirts --\n')

def make_shirt(text = 'I love Python', size = 'L'):
    print(f'You want a t-shirt with text \'{text}\' size {size}')

make_shirt()
make_shirt(size = 'M', text = 'Java')