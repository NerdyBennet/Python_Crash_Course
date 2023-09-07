print("The original list:")
menu_items = ('- burger', '- pizzas', '- fries', '- chicken wings', '- wraps')
for restaurant_items in menu_items:
    print(restaurant_items.title())
# menu_items[0] = 'hotdog' # doesn't work
print("\nThe overwritten list:")
menu_items = ('- burger', '- pizza', '- fries', '- sandwiches' ,'- noodles')
for restaurant_items in menu_items:
    print(restaurant_items.title())