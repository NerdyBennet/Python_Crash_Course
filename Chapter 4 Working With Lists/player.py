players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3]) # slice 0 through 2
print(players[:4]) # starts at the beginning of the list, ends at the
# fourth
print(players[2:]) # starts at the end of the list
print(players[-3:]) # prints the last 3 elements of a list
# 1. value in a slice = start
# 2.value in a slice = stop
# 3. value in a slice determines how many elements to skip between items 
# in the specified range

print('Here are the first three players on my team:')
for player in players[:3]:
    print(player.title())

print('The first three items in the list "players" are:')
print(players[:3])

print('\nThe first 3 items of the middle of the list "players" are:')
print(players[1:4])

print('\nThe last 3 items in the list "players" are:')
print(players[2:])