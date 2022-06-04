'''Class for restaraunt'''
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