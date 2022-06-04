'''9.13. Кубики: создайте класс Die с одним атрибутом sides, который имеет
значение по умолчанию 6. Напишите метод roll_die() для вывода случайного числа 
от 1 до количества граней на кубике. Создайте экземпляр, представляющий
6-гранный кубик, и смоделируйте 10 бросков. Создайте экземпляры, представляющие
10- и 20-гранный кубик. Смоделируйте 10 бросков каждого кубика.'''

from random import randint


class Die():

    def __init__(self, sides = 6):
        self.sides = sides
    
    def roll_die(self, times = 1):
        print(f'Rolling die with {self.sides} sides {times} times')
        for roll in range(times):
            roll =  randint(1, self.sides)
            print(f'Number {roll}!')

die_1 = Die()
die_1.roll_die(10)

die_2 = Die(10)
die_2.roll_die(10)


die_3 = Die(20)
die_3.roll_die(10)