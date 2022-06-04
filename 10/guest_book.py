'''10.4. Гостевая книга: напишите цикл while, который запрашивает у
пользователей имена. При вводе каждого имени выведите на экран приветствие и
добавьте строку с сообщением в файл с именем guest_book.txt. Проследите за тем,
чтобы каждое сообщение размещалось в отдельной строке файла.'''

file_name = 'guest_book.txt'

while True:
    name = input('Enter your name:')
    name_message = f'Hi {name}! I\'m glad to see you!\n'
    print(name_message)
    with open(file_name, 'a') as doc:
        doc.write(name_message)