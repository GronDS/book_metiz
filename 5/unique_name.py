'''5.10. Проверка имен пользователей: выполните следующие действия для 
создания программы, моделирующей проверку уникальности имен пользователей.
• Создайте список current_users, содержащий пять и более имен пользователей.
• Создайте другой список, new_users, содержащий пять имен пользователей. 
Убедитесь в том, что одно или два новых имени также присутствуют 
в списке current_users.
• Переберите список new_users и для каждого имени в этом списке проверьте,
было ли оно использовано ранее. Если имя уже использовалось, выведите 
сообщение о том, что пользователь должен выбрать новое имя. 
Если имя не использовалось, выведите сообщение о его доступности.
• Проследите за тем, чтобы сравнение выполнялось без учета регистра символов.
Если имя 'John' уже используется, в регистрации имени 'JOHN' следует отказать.
(Для этого необходимо создать копию current_users, 
содержащую версию всех существующих имен пользователей в нижнем регистре.)'''

current_users = ['user123', 'admin', 'FunnyCrab99', 'admin2', 'AngryTr0ll',
'MrNoone', 'dasjd12', 'jokER15']

current_lower = []

for user in current_users:
    current_lower.append(user.lower())

new_users = ['MrNoone','ADmin2','1MindBlow1','dsadasd1','34123458']

if new_users:
    for new_user in new_users:
        if new_user.lower() in current_lower:
            print(f'Nick {new_user} is already taken! Nick must be unique.')
        else:
            print(f'{new_user} is available nickname.')
else:
    print('No more new users.')
