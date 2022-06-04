'''10.8. Кошки и собаки: создайте два файла с именами cats.txt и dogs.txt. 
Сохраните по крайней мере три клички кошек в первом файле и три клички собак 
во втором. Напишите программу, которая пытается прочитать эти файлы и выводит
их содержимое на экран. Заключите свой код в блок try-except для перехвата 
исключения FileNotFoundError и вывода понятного сообщения об отсутствии файла.
Переместите один из файлов в другое место файловой системы; убедитесь в том, 
что код блока except выполняется как положено.'''

cats = 'cats.txt'
dogs = 'dogs.txt'
filenames = [cats, dogs]

for file_ in filenames:
    try:
        with open(file_) as f:
            print(f'Reading {file_}:\n{f.read()}\n')
    except FileNotFoundError:
        print(f'File {file_} not found!')