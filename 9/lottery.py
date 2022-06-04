'''9.14. Лотерея: создайте список или кортеж, содержащий серию из 10 чисел и
5 букв. Случайным образом выберите 4 числа или буквы из списка. Выведите
сообщение о том, что билет, содержащий эту комбинацию из четырех цифр или букв,
является выигрышным.'''

from random import choices

keys = ('A', 'B', 'C', 'D', 'E', 1, 2, 3, 4, 5, 6, 7, 8, 9, 0)

# win_keys = []

# for key in range(4):
#     key = choice(keys)
#     win_keys.append(key)

# print (win_keys)

win_keys = choices(population = keys, k= 4)
print(win_keys)
