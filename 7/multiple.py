'''7.3. Числа, кратные 10: запросите у пользователя число и сообщите,
кратно оно 10 или нет.'''

number = input('Enter the number, please : ')
number = int(number)
if number%10 == 0:
    print (f'The number {number} is a multiple of 10')
else:
    print (f'The number {number} is not a multiple of 10')