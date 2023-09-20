age = 18
if age < 4: # if-elif-else allows you to test for one specific condition
    price = 0
elif age < 18: # elif = else if
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20
print(f"Your admission cost is {price}.")