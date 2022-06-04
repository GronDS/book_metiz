'''10.10. Частые слова: зайдите на сайт проекта «Гутенберг» 
(http://gutenberg.org/) и найдите несколько книг для анализа. Загрузите
текстовые файлы этих произведений или скопируйте текст из браузера в текстовый
файл на вашем компьютере. Для подсчета количества вхождений слова или выражения
в строку можно воспользоваться методом count(). Обратите внимание: 
преобразование строки к нижнему регистру функцией lower() позволяет найти все
вхождения искомого слова независимо от регистра. Напишите программу, которая 
читает файлы из проекта «Гутенберг» и определяет количество вхождений слова 
'the' в каждом тексте. Результат будет приближенным, потому что программа также
будет учитывать такие слова, как 'then' и 'there'. Попробуйте повторить поиск 
для строки 'the ' (с пробелом в строке) и посмотрите, насколько уменьшится
количество найденных результатов.'''

books = ['pg68131.txt', 'pg68132.txt', 'pg68133.txt', 'pg68134.txt']

for book in books:
    try:
        with open(book) as b:
            book_text = b.read()
            counter = book_text.lower().count('the ')
            print(f'File {book} counts {counter} "the" ')
    except FileNotFoundError:
        print (f'File {book} not found in this directory!')