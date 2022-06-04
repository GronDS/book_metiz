'''10.9. Ошибки без уведомления: измените блок except из упражнения 10.8 так,
чтобы при отсутствии файла программа продолжала работу, не уведомляя
пользователя о проблеме.'''

cats = 'cats.txt'
dogs = 'dogs.txt'
filenames = [cats, dogs]

for file_ in filenames:
    try:
        with open(file_) as f:
            print(f'Reading {file_}:\n{f.read()}\n')
    except FileNotFoundError:
        pass