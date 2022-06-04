'''9.12. Множественные модули: сохраните класс User в одном модуле, а классы
Privileges и Admin в другом модуле. В отдельном файле создайте экземпляр
Admin и вызовите метод show_privileges(), чтобы показать, что все работает 
правильно.'''

from admin import Privileges, Admin as A

adminus = A('Angry', 'Adminus', '22', 'UK', 'London')

adminus.privileges.show_privileges()