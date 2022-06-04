'''6.10. Любимые числа: измените программу из упражнения 6.2, 
чтобы для каждого человека можно было хранить более одного любимого числа.
Выведите имя каждого человека в списке и его любимые числа.'''

fav_nums = {
    'google' : [87, 53, 92, 44],
    'randomus' : [71, 77, 19, 79, 52],
    'randstuff' : [81, 70, 11],
    'randomorg' : [52, 12, 71],
    'gigacalculator' : [69, 78, 32],    
    }

for source, nums in fav_nums.items():
    print(f'\nThis is the results of RNG in range from 1 to 100 from {source}:')
    print(nums)