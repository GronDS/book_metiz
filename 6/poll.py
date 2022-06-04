'''6.6. Опрос: возьмите за основу код favorite_languages.py .
• Создайте список людей, которые должны участвовать в опросе по поводу 
любимого языка программирования. Включите некоторые имена, которые уже 
присутствуют в списке, и некоторые имена, которых в списке еще нет.
• Переберите список людей, которые должны участвовать в опросе. Если они уже
прошли опрос, выведите сообщение с благодарностью за участие. Если они еще не
проходили опрос, выведите сообщение с предложением принять участие.'''

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

poll = ['sarah', 'andrew', 'phil', 'tom', 'ann']

for name in poll:
    if name in favorite_languages.keys():
        print(f"{name.title()}'s favorite language is {favorite_languages[name].title()}")
    else:
        print(f'{name.title()}, please take part in our survey')