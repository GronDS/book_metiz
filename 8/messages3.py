'''8.11. Архивированные сообщения: начните с программы из упражнения 8.10.
Вызовите функцию send_messages() для копии списка сообщений. После вызова
функции выведите оба списка и убедитесь в том, что в исходном списке остались 
все сообщения.'''

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


send_messages(messages[:])

print('\nShowing lists:')
print(messages)
print(sended_messages)