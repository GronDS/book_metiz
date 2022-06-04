'''5.6. Периоды жизни: напишите цепочку if-elif-else для определения периода
жизни человека. Присвойте значение переменной age, а затем выведите 
сообщение:
• Если значение меньше 2 — младенец.
• Если значение больше или равно 2, но меньше 4 —  малыш.
• Если значение больше или равно 4, но меньше 13 —  ребенок.
• Если значение больше или равно 13, но меньше 20 —  подросток.
• Если значение больше или равно 20, но меньше 65 —  взрослый.
• Если значение больше или равно 65 —  пожилой человек'''
age = 54

if age < 2:
    name = 'Infant'
elif age <4:
    name = 'Baby'
elif age <13:
    name = 'Child'
elif age <20:
    name = 'Teenager'
elif age <65:
    name = 'Grown man'
elif age >= 65:
    name = 'Old мan'

print(f'You are {age} years old. I will call you a {name.lower()}')