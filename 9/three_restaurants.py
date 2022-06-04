'''9.2. Три ресторана: начните с класса из упражнения 9.1.
Создайте три разных экземпляра, вызовите для каждого экземпляра метод
describe_restaurant().'''

class Restaraunt():

    def __init__(self, restaurant_name, cuisine_type):
        self.r_name = restaurant_name.title()
        self.c_type = cuisine_type.title()
    
    def describe_restaurant(self):
        print(f'\nThe restaraunt name is "{self.r_name}"')
        print(f'Type of cuisine {self.c_type}')
    
    def open_restaraunt(self):
        print(f'\nRestaraunt {self.r_name} is open')


rest_1 = Restaraunt('legran', 'french')
rest_2 = Restaraunt('PALERMO', 'italian')
rest_3 = Restaraunt('AQ Kitchen', 'molecular')

rest_1.describe_restaurant()
rest_2.describe_restaurant()
rest_3.describe_restaurant()