'''5.11. Порядковые числительные: порядковые числительные в английском языке
заканчиваются суффиксом th (кроме 1st, 2nd и 3rd).
• Сохраните числа от 1 до 9 в списке.
• Переберите элементы списка.
• Используйте цепочку if-elif-else в цикле для вывода правильного окончания
числительного для каждого числа. Программа должна выводить числительные 
"1st 2nd 3rd 4th 5th 6th 7th 8th 9th", причем каждый результат должен
располагаться в отдельной строке.'''

nums = [num for num in range(1,10)]
if nums:
    for ordinal_num in nums:
        if ordinal_num == 1:
            print(f'{ordinal_num}st')
        elif ordinal_num == 2:
            print(f'{ordinal_num}nd')
        elif ordinal_num == 3:
            print(f'{ordinal_num}rd')
        else:
            print(f'{ordinal_num}th')
else:
    print('No nums')