'''6.4. Глоссарий 2: теперь, когда вы знаете, как перебрать элементы словаря, 
упростите код из упражнения 6.3, заменив серию команд print циклом,
перебирающим ключи и значения словаря. Когда вы будете уверены в том, 
что цикл работает, добавьте в глоссарий еще пять терминов Python. 
При повторном запуске программы новые слова и значения должны
быть автоматически включены в вывод.'''

glossary = {
    'variable' : 'это символьное имя, которое является ссылкой или указателем на объект.',
    'constant' : 'переменная, значение которой остается неизменным на протяжении всего срока жизни программы',
    'list' : 'упорядоченная изменяемая коллекция объектов произвольных типов',
    'tuple' : 'неизменяемый список.',
    'slice' : 'подмножество элементов списка',
    'dict' : 'неупорядоченная коллекция произвольных объектов с доступом по ключу.',
    'set' : '"контейнер", содержащий не повторяющиеся элементы в случайном порядке.',
    'PEP 8' : 'руководство по стилю кода Python .',
    'string' : 'последовательность символов, являющаяся неизменной и записываемая в одинарных или двойных кавычках .',
    'Zen of Python' : 'определённая философия программирования.Вызывается командой «import this»',
}

for term in glossary:
    print(f'{term} :\n\t {glossary[term]}\n')