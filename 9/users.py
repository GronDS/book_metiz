'''9.3. Пользователи: создайте класс с именем User. Создайте два атрибута 
first_name и last_name, а затем еще несколько атрибутов, которые обычно 
хранятся в профиле пользователя. Напишите метод describe_user(), который 
выводит сводку с информацией о пользователе. Создайте еще один метод 
greet_user() для вывода персонального приветствия для пользователя.
Создайте несколько экземпляров, представляющих разных пользователей. Вызовите 
оба метода для каждого пользователя.'''

class User():

    def __init__(self, first_name, last_name, age, country, city):
        self.first = first_name.title()
        self.last = last_name.title()
        self.age = age
        self.country = country
        self.city = city.title()

    def describe_user(self):
        print('User info:')
        print(f"-Name : {self.first}\
            \n-Surname: {self.last}\
            \n-Age: {self.age}\
            \n-Country: {self.country}\
            \n-City: {self.city}\n ")
    
    def greet_user(self):
        print(f'Welcome, {self.first} {self.last}!\n')

user_0 = User('Admin', 'Mode', 54, 'Spain', 'Madrid')
user_0.describe_user()
user_0.greet_user()

user_1 = User('New', 'User', 21, 'USA', 'New-York')
user_1.describe_user()
user_1.greet_user()