'''8.2. Любимая книга: напишите функцию favorite_book(), которая получает один
параметр title. Функция должна выводить сообщение вида 
«One of my favorite books is Alice in Wonderland».
Вызовите функцию и убедитесь в том, что название книги правильно передается 
как аргумент при вызове функции.'''

def favorite_book(title):
    print(f'One of my favorite books is {title}')

favorite_book('War and Peace')