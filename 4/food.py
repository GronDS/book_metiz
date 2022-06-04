my_foods = ['pizza', 'falafel', 'carrot cake']

friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

# print("My favorite foods are:")
# print(my_foods)

# print("\nMy friend's favorite foods are:")
# print(friend_foods)

'''4.12. Больше циклов: во всех версиях foods.py из этого раздела мы избегали 
использования цикла for при выводе для экономии места.
Выберите версию foods.py и напишите два цикла for для вывода каждого списка.'''

print("\nMy favorite foods are:")
for food in my_foods:
    print(food)

print("\nMy friend's favorite foods are:")
for friend_food in friend_foods:
    print(friend_food)