'''9.7. Администратор: администратор — особая разновидность пользователя. 
Напишите класс с именем Admin, наследующий от класса User из упражнения 9.3 или
упражнения 9.5 (с. 180). Добавьте атрибут privileges для хранения списка строк 
вида "разрешено добавлять сообщения", "разрешено удалять пользователей", 
"разрешено банить пользователей" и т. д. Напишите метод show_privileges() для
вывода набора привилегий администратора. Создайте экземпляр Admin и вызовите 
свой метод.'''

class User():

    def __init__(self, first_name, last_name, age, country, city):
        self.first = first_name.title()
        self.last = last_name.title()
        self.age = age
        self.country = country
        self.city = city.title()
        self.login_attempts = 0

    def describe_user(self):
        print('User info:')
        print(f"-Name : {self.first}\
            \n-Surname: {self.last}\
            \n-Age: {self.age}\
            \n-Country: {self.country}\
            \n-City: {self.city}\n ")
    
    def greet_user(self):
        print(f'Welcome, {self.first} {self.last}!\n')

    def increment_login_attempts(self):
        print('Login attempt...')
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        print('Login attempts have been reset')
        self.login_attempts = 0

class Admin(User):
    
    def __init__(self, first_name, last_name, age, country, city):
        super().__init__(first_name, last_name, age, country, city)
        self.first = first_name
        self.last = last_name
        self.privileges = ['add post', 'delete post', 'ban user']

    def show_privileges(self):
        print(f'{self.first} {self.last} privileges:')
        for privelege in self.privileges:
            print(f'- can {privelege}')

admin = Admin('Angry', 'Adminus', 54, 'Australia', 'Sydney')
admin.show_privileges()