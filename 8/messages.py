'''8.9. Сообщения: создайте список с серией коротких сообщений.
Передайте список функции show_messages(),
которая выводит текст каждого сообщения в списке.'''

messages = ['Hi, friend!', 'What\'s up?', 'Let\'s meet tonight at 8pm',
'How do you feel?']

def show_messages(message):
    for message in messages:
        print(message)

show_messages(messages)