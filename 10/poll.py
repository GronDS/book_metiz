'''10.5. Опрос: напишите цикл while, в котором программа спрашивает у
пользователя, почему ему нравится программировать. Каждый раз, когда
пользователь вводит очередную причину, сохраните текст его ответа в файле.'''

file_name = 'poll.txt'

while True:
    answer = input('Why you like programming? ')
    with open(file_name, 'a') as doc:
        doc.write(f'{answer}\n')