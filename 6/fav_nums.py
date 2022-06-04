'''6.2. Любимые числа: используйте словарь для хранения любимых чисел.
Возьмите пять имен и используйте их как ключи словаря. 
Придумайте любимое число для каждого человека и сохраните его как 
значение в словаре. Выведите имя каждого человека и его любимое число.
Чтобы задача стала более интересной, опросите нескольких друзей и соберите
реальные данные для своей программы.'''

fav_nums = {
    'google' : 87,
    'randomus' : 71,
    'randstuff' : 81,
    'random' : 52,
    'gigacalculator' : 69,    
    }

print('This is the result of RNG in range from 1 to 100:')

print(f"google.com : {fav_nums['google']}")
print(f"randomus.ru : {fav_nums['randomus']}")
print(f"randstuff.ru : {fav_nums['randstuff']}")
print(f"random.org : {fav_nums['random']}")
print(f"gigacalculator.com : {fav_nums['gigacalculator']}")