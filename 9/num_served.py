'''9.4. Посетители: начните с программы из упражнения 9.1 (с. 175). Добавьте
атрибут number_served со значением по умолчанию 0; он представляет количество
обслуженных посетителей. Создайте экземпляр с именем restaurant. Выведите 
значение number_served, потом измените и выведите снова. Добавьте метод с 
именем set_number_served(), позволяющий задать количество обслуженных 
посетителей. Вызовите метод с новым числом, снова выведите значение.
Добавьте метод с именем increment_number_served(), который увеличивает
количество обслуженных посетителей на заданную величину.
Вызовите этот метод с любым числом, которое могло бы представлять количество
обслуженных клиентов, —  скажем, за один день.'''

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
        



restaurant = Restaraunt('las torres','spanish')
restaurant.describe_restaurant()

print(restaurant.number_served)
restaurant.number_served = 1
restaurant.show_number_served()

restaurant.set_number_served(1000)
restaurant.show_number_served()

restaurant.increment_number_served(52)
restaurant.show_number_served()

