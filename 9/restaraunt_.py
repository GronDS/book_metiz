'''9.1. Ресторан: создайте класс с именем Restaurant. Метод __init__() класса
Restaurant должен содержать два атрибута: restaurant_name и cuisine_type.
Создайте метод describe_restaurant(), который выводит два атрибута, и метод
open_restaurant(), который выводит сообщение о том, что ресторан открыт.
Создайте на основе своего класса экземпляр с именем restaurant.
Выведите два атрибута по отдельности, затем вызовите оба метода.'''

class Restaraunt():

    def __init__(self, restaurant_name, cuisine_type):
        self.r_name = restaurant_name.title()
        self.c_type = cuisine_type.title()
    
    def describe_restaurant(self):
        print(f'\nThe restaraunt name is "{self.r_name}"')
        print(f'Type of cuisine {self.c_type}')
    
    def open_restaraunt(self):
        print(f'\nRestaraunt {self.r_name} is open')



rest_0 = Restaraunt('las torres','spanish')

print(rest_0.r_name)
print(rest_0.c_type)

rest_0.describe_restaurant()
rest_0.open_restaraunt()