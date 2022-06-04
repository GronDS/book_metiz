'''10.2. Изучение C: метод replace() может использоваться для замены любого 
слова в строке другим словом. В следующем примере слово 'dog' заменяется словом
'cat':
>>> message = "I really like dogs."
>>> message.replace('dog', 'cat')
'I really like cats.'
Прочитайте каждую строку из только что созданного файла learning_python.txt и 
замените слово Python названием другого языка, например C. Выведите каждую
измененную строку на экран.'''

file_name = 'learning_python.txt'
with open(file_name) as my_text:
    for line in my_text:
        message_ = line.rstrip()
        print(message_.replace('Python', 'C'))