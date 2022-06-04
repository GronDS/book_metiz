'''Class for userinfo'''

from user import User

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