'''9.5. Попытки входа: добавьте атрибут login_attempts в класс User из упражнения
9.3 (с. 175). Напишите метод increment_login_attempts(), увеличивающий значение
login_attempts на 1. Напишите другой метод с именем reset_login_attempts(),
обнуляющий значение login_attempts. Создайте экземпляр класса User и вызовите
increment_login_attempts() несколько раз. Выведите значение login_attempts,
чтобы убедиться в том, что значение было изменено правильно, а затем вызовите 
reset_login_attempts(). Снова выведите login_attempts и убедитесь в том, что
значение обнулилось.'''

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

user_0 = User('Admin', 'Mode', 54, 'Spain', 'Madrid')

print(f'Login Attempts: {user_0.login_attempts}')
user_0.increment_login_attempts()
user_0.increment_login_attempts()
user_0.increment_login_attempts()
user_0.increment_login_attempts()

print(f'Login Attempts: {user_0.login_attempts}')
user_0.reset_login_attempts()
print(f'Login Attempts: {user_0.login_attempts}')