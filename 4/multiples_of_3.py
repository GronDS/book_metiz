'''4.7. Тройки: создайте список чисел, кратных 3, в диапазоне от 3 до 30. 
Выведите все числа своего списка в цикле for.'''


multiples = [num for num in range(3,31,3)]
for var in multiples:
    print(var)