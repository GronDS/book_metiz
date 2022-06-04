'''10.12. Сохраненное любимое число: объедините две программы из упражнения 
10.11 в один файл. Если число уже сохранено, сообщите его пользователю, а если 
нет —  запросите любимое число пользователя и сохраните в файле. Выполните
программу дважды, чтобы убедиться в том, что она работает.'''

import json

file_name = 'fav_num.json'

def check_file():
    try:
        with open(file_name) as f:
            fav_num = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return fav_num

def new_num():
    fav_num = input('Enter your favorite number:')
    with open(file_name, 'w') as f:
        json.dump(fav_num, f)
    print(f'Number {fav_num} successfully recorded to the {file_name}')
    return fav_num

def show_num():
    if check_file():
        fav_num = check_file()
        print(f'I know your favorite number! It\'s {fav_num}')
    else:
        new_num()

show_num()