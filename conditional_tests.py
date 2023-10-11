car = 'toyota'
cars = ['lamborghini', 'audi', 'mercedes']
age1 = 19
age2 = 20
age3 = 21

if car.lower() == 'toyota':
    print('\nThe name of the car brand is "toyota" in lowercase.')
else:
    print('\nThe name of the car brand is not "toyota" in lowercase.')

if car.lower() != 'toyota':
    print('\nThe name of the car brand is not "toyota" in lowercase.')
else:
    print('\nThe name of the car brand is "toyota" in lowercase.')

if car.upper() == 'toyota':
    print('\nThe name of the car brand is "toyota" in uppercase.')
else:
    print('\nThe name of the car brand is "toyota" in lowercase.')

if 'Toyota' in car: # in (=) ==
    print('"Toyota" is in the list car')
else:
    print('"Toyota" is not in the list car')

if 'Toyota' != car: # not in (=) !=
    print('"Toyota" is not in the list car')
else:
    print('"Toyota" is in the list car')

if 'toyota' in car:
    print('"toyota" is in the list car')
else:
    print('"toyota" is not in the list car')
if age1 < 21:
    print("\nSorry, you are not old enough.")
else:
    print("\nYou are old enough!")

if age2 < 21:
    print("\nSorry, you are not old enough.")
else:
    print("\nYou are old enough!")

if age3 < 21:
    print("\nSorry, you are not old enough.")
else:
    print("\nYou are old enough!")

if age1 and age3 <= 21: # both need to be 21 or older for it to be true
    print("\nSorry, you are not old enough.")

if age1 or age3 >= 21: # if either of them are 21 or older it's true
    print("You are old enough!")
else:
    print("Sorry you are not old enough.")
print("\nIs car == 'toyota'? I guess not.") # 1
print(car == 'subaru')

print("\nIs car == 'toyota'? I guess so.") # 2
print(car == 'toyota')

print("\nIs car == 'toyota'? I guess so.") # 3
print(car != 'audi')

print("\nIs car == 'toyota'? I guess not.") # 4
print(car == 'mercedes')

print("\nIs car == 'toyota'? I guess not.") # 5 
print(car == 'honda')

print("\nIs car == 'toyota'? I guess not.") # 6
print(car == 'lamborghini')

print("\nIs car == 'toyota'? I guess not.") # 7
print(car == 'toyota')

print("\nIs car != 'toyota'? I guess so.") # 8
print(car != 'porsche')

print("\nIs car != 'toyota'? I guess so.") # 9
print(car == 'toyota')

print("\nIs car == 'toyota'? I guess not.") # 10
print(car == 'ford')