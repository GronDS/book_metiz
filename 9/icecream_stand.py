'''9.6. Киоск с мороженым: киоск с мороженым — особая разновидность ресторана. 
Напишите класс IceCreamStand, наследующий от класса Restaurant из упражнения
9.1 (с. 175) или упражнения 9.4 (с. 180). Подойдет любая версия класса; просто 
выберите ту, которая вам больше нравится. Добавьте атрибут с именем flavors для
хранения списка сортов мороженого. Напишите метод, который выводит этот список.
Создайте экземпляр IceCreamStand и вызовите этот метод.'''

class Restaraunt():

    def __init__(self, restaurant_name, cuisine_type):
        self.r_name = restaurant_name.title()
        self.c_type = cuisine_type.title()
        self.number_served = 0
        
    def describe_restaurant(self):
        print(f'\nThe restaraunt name is "{self.r_name}".')
        print(f'Type of cuisine {self.c_type}.')

    
    def open_restaraunt(self):
        print(f'\nRestaraunt {self.r_name} is open!')

    def show_number_served(self):
        print(f'Served {self.number_served} people.')

    def set_number_served(self, set):
        self.number_served = set

    def increment_number_served(self, increment):
        self.number_served += increment

class IceCreamStand(Restaraunt):

    def __init__(self, restaurant_name, cuisine_type='ice cream'):
        super().__init__(restaurant_name, cuisine_type)
        self.restaurant_name = restaurant_name
        self.flavors = ['Vanilla', 'Chocolate', 'Chocolate Chip',
        'Butter Pecan','Chocolate Chip Cookie Dough', 'Eggnog', 'Eskimo',
        'Strawberry']
    
    def show_flavors (self):
        print(f'The current list of flavors in  {self.restaurant_name}:\
            \n{self.flavors}')

mister_softee = IceCreamStand('Mister Softee', 'Ice Cream Stand')
mister_softee.flavors = ['Chocolate', 'Vanilla']
mister_softee.describe_restaurant()
mister_softee.show_flavors()