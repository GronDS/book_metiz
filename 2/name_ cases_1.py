'''2.3. Личное сообщение: сохраните имя пользователя в переменной и выведите
сообщение, предназначенное для конкретного человека.
Сообщение должно быть простым — например, 
«Hello Eric, would you like to learn some Python today?”.'''

'''2.4. Регистр символов в именах: сохраните имя пользователя в переменной и
выведите его в нижнем регистре, в верхнем регистре и с капитализацией начальных
букв каждого слова.'''

name = 'gRoN'
message_ = f'Hello {name}, would you like to learn some Python today?'
message_1 = f'Hello {name.lower()}, would you like to learn some Python today?'
message_2 = f'Hello {name.upper()}, would you like to learn some Python today?'
message_3 = f'Hello {name.title()}, would you like to learn some Python today?'
print(f'{message_}\n{message_1}\n{message_2}\n{message_3}')