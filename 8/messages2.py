'''8.10. Отправка сообщений: начните с копии вашей программы из упражнения 8.9. 
Напишите функцию send_messages(), которая выводит каждое сообщение и перемещает
его в новый список с именем sent_messages.
После вызова функции выведите оба списка и убедитесь в том, что перемещение
прошло успешно.'''

messages = ['Hi, friend!', 'What\'s up?', 'Let\'s meet tonight at 8pm',
'How do you feel?']

sended_messages = []

def show_messages(message):
    print('Messages for send:')
    for message in messages:
        print(message)

show_messages(messages)

def send_messages(messages):
    print('\nSending messages:')
    while messages:
        message = messages.pop()
        print(message)
        sended_messages.append(message)

send_messages(messages)

print('\nShowing lists:')
print(messages)
print(sended_messages)