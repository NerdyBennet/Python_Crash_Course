players = ['charles', 'martina', 'micheal', 'florence', 'eli']
print(players[0:3]) # slice 0 through 2
print(players[:4]) # omit the the first index and it starts at the beginning of the list
print(players[2:]) # and the other way around
print(players[-3:]) # prints the last 3 elements of a list
# 1. value in a slice = start; 2.value in a slice = stop; 3. value in a slice how many to skip between items in the specified range
print('Here are the first three players on my team:')
for player in players[:3]:
    print(player.title())