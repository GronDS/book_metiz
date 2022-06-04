'''10.11. Любимое число: напишите программу, которая запрашивает у пользователя
его любимое число. Воспользуйтесь функцией json.dump() для сохранения этого
числа в файле. Напишите другую программу, которая читает это значение и выводит
сообщение: «Я знаю ваше любимое число! Это _____».(fav_num_check.py)'''

import json

fav_number = input('Enter your favorite number:')

file_name = 'fav_number.json'
with open(file_name, 'w') as f:
    json.dump(fav_number, f)