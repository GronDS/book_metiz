'''10.13. Проверка пользователя: последняя версия remember_me.py предполагает,
что пользователь либо уже ввел свое имя, либо программа выполняется впервые. Ее
нужно изменить на тот случай, если текущий пользователь не является тем
человеком, который последним использовал программу. Прежде чем выводить 
приветствие в greet_user(), спросите, правильно ли определено имя пользователя.
Если ответ будет отрицательным, вызовите get_new_username() для получения
правильного имени пользователя.'''

import json

def get_stored_username():
    """Get stored username if available."""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name?")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    print(f"We'll remember you when you come back, {username}!")
    return username

def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        name = input(f'Is your name {username}(y/n)?')
        if name == 'y':
            print(f"Welcome back, {username}!")
        elif name == 'n':
            username = get_new_username()
        else :
            print('Incorrect input!')
    else:
        username = get_new_username()


greet_user()