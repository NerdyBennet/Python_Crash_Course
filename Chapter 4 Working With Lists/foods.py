my_foods = ['pizza', 'doner' , 'carrot cake']
friend_foods = my_foods[:] # starts at the first index and ends at the end
#friend_foods = my_foods[] # This doesn't work 

# prove that they are two separate lists
my_foods.append('burger')
friend_foods.append('ice cream')


print('My favourite foods are:')
print(my_foods)

print("\nMy friend's foods are:")
print(friend_foods)