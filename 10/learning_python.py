'''10.1. Изучение Python: откройте пустой файл в текстовом редакторе и напишите
несколько строк текста о возможностях Python. Каждая строка должна начинаться с
фразы «In Python you can…». Сохраните файл под именем learning_python.txt в
каталоге, использованном для примеров этой главы. Напишите программу, которая
читает файл и выводит текст три раза: с чтением всего файла, с перебором строк
объекта файла и с сохранением строк в списке с последующим выводом списка вне
блока with.'''

print('-- reading in the entire file --')
file_name = 'learning_python.txt'
with open(file_name) as my_text:
    print(my_text.read())

print('-- looping over the file object --')

with open(file_name) as my_text:
    for line in my_text:
        print(line.rstrip())


with open(file_name) as my_text:
    file_list = my_text.readlines()
    
print('-- storing the lines in a list --')

for line in file_list:
    print(line.rstrip())