'''8.15. Печать моделей: выделите функции примера print_models.py в отдельный 
файл с именем printing_functions.py. Разместите команду import в начале файла
print_models.py и измените файл так, 
чтобы в нем использовались импортированные функции.'''

from printing_functions import print_models, show_completed_models as show

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show(completed_models)