'''10.7. Калькулятор: заключите код из упражнения 10.6 в цикл while, чтобы пользователь
мог продолжать вводить числа, даже если он допустил ошибку и ввел текст вместо числа.'''

while True:
    try:
        first_value = float(input('Enter the 1st number:'))
        second_value = float(input('Enter the 2nd number:'))
    except ValueError:
        print('The entered value is invalid! Try again!\n')
    else:
        summ = first_value + second_value
        print(f'Result: {first_value} + {second_value} = {summ}\n')