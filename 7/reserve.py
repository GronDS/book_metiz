'''7.2. Заказ стола: напишите программу, которая спрашивает у пользователя,
на сколько мест он хочет забронировать стол в ресторане.
Если введенное число больше 8, выведите сообщение о том, что пользователю
придется подождать. В противном случае сообщите, что стол готов.'''

reserve = input('How many people would you like to book a table for? ')
reserve = int(reserve)
if reserve > 8 :
    print('You will have to wait for your table.')
else:
    print('Your table is ready!')