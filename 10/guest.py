'''10.3. Гость: напишите программу, которая запрашивает у пользователя его имя.
Введенный ответ сохраняется в файле с именем guest.txt.'''

guest_name = input('Enter your name:')

file_name = 'guest.txt'
with open(file_name, 'w') as doc:
    doc.write(guest_name)