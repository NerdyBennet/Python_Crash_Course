my_foods = ['pizza', 'doner' , 'carrot cake']
friends_foods = my_foods[:] # starts at the first index and ends at the
# end

# friends_foods = my_foods[] # This doesn't work 

# prove that they are two separate lists
my_foods.append('burger')
friends_foods.append('ice cream')

print('My favourite foods are:')
for my_favourite_foods in my_foods:
    print(my_favourite_foods)

print("\nMy friend's foods are:")
for my_friends_favourite_foods in friends_foods:
    print(my_friends_favourite_foods)