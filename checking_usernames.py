current_users = ['xgamer', 'John', 'Tyler_Durden', 'xxIron_ballsxx',
'drake_the_type_of_guy'
]
current_users = ['xgamer', 'john', 'tyler_durden', 'xxiron_ballsxx',
'drake_the_type_of_guy'
]

new_users = ['noire_havok', 'nuke_gamer', 'john', 'fire_skull',
'the_ultimate.gamer'
]

for new_user in new_users:
    if new_user in current_users:
        print("Enter a new username!")
    else:
        print("That username is available.")
