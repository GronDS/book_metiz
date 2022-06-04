'''5.8. Hello Admin: создайте список из пяти и более имен пользователей,
включающий имя 'admin'. Представьте, что вы пишете код, который выводит
приветственное сообщение для каждого пользователя после его входа на сайт.
Переберите элементы списка и выведите сообщение для каждого пользователя:
• Для пользователя с именем 'admin' выведите особое сообщение — 
например, «Hello admin, would you like to see a status report?».
• В остальных случаях выводите универсальное приветствие — например,
«Hello Jaden, thank you for logging in again».'''

'''5.9. Без пользователей: добавьте в hello_admin.py команду if, 
которая проверит, что список пользователей не пуст.
• Если список пуст, выведите сообщение «We need to ind some users!».
• Удалите из списка все имена пользователей и убедитесь в том,
что программа выводит правильное сообщение.'''


usernames = ['user123','admin','FunnyCrab99','admin2','AngryTr0ll']
# usernames = []

if usernames:
    for user in usernames:
        if user == 'admin':
            print('Hello admin, would you like to see a status report?')
        else:
            print(f'Hello {user}, thank you for logging in again')
else:
    print('We need to find some users')