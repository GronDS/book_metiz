'''9.10. Импортирование класса Restaurant: возьмите последнюю версию класса
Restaurant и сохраните ее в модуле. Создайте отдельный файл, импортирующий 
класс Restaurant. Создайте экземпляр Restaurant и вызовите один из методов
Restaurant, чтобы показать, что команда import работает правильно.'''

from restaraunt import Restaraunt as R

las_torres = R('las torres','spanish')
las_torres.describe_restaurant()

print(las_torres.number_served)
las_torres.number_served = 1
las_torres.show_number_served()

las_torres.set_number_served(1000)
las_torres.show_number_served()

las_torres.increment_number_served(52)
las_torres.show_number_served()