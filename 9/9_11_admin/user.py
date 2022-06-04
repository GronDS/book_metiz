'''Class for userinfo'''

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

class Privileges():
    
    def __init__(self) :
        self.privileges = ['add post', 'delete post', 'ban user']
    
    def show_privileges(self):
        print('User privileges:')
        for privelege in self.privileges:
            print(f'- can {privelege}')

class Admin(User):
    
    def __init__(self, first_name, last_name, age, country, city):
        super().__init__(first_name, last_name, age, country, city)
        self.first = first_name
        self.last = last_name
        self.privileges = Privileges()