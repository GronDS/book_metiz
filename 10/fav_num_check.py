'''10.11(2) Напишите другую программу, которая читает это значение и выводит
сообщение: «Я знаю ваше любимое число! Это _____».'''

import json

file_name = 'fav_number.json'
with open(file_name) as f:
    fav_number = f.read()
    print(f'I know your favorite number! It\'s {fav_number}')