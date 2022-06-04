'''9.11. Импортирование класса Admin: начните с версии класса из упражнения 9.8
(с. 186). Сохраните классы User, Privileges и Admin в одном модуле. Создайте
отдельный файл, создайте экземпляр Admin и вызовите метод show_privileges(),
чтобы показать, что все работает правильно.'''

from user import User , Privileges, Admin as A

admin = A('Angry', 'Adminus', '22', 'UK', 'London')

admin.privileges.show_privileges()