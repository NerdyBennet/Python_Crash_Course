pizza = ['pepperoni','salami','bolognese']
for pizzas in pizza:
    print(pizzas)
    print(f"I like pizza with {pizzas}!")

print('\nI also like pizza Hawaii')
print('\nAnd I like pizzas with mushrooms on it!')
print('\nI really love doner sauce on my pizza!')


friends_pizzas = pizza[:]
friends_pizzas.append('napoletana')
pizza.append('margherita')
print("\nMy favourite pizza's are:")
for my_pizzas in pizza:
    print(my_pizzas)

print("\nMy friend's favourite pizzas are:")
for my_friends_pizzas in friends_pizzas:
    print(my_friends_pizzas)