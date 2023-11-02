usernames = ['kevinthegamer', 'nerdybennet', 'admin', 'xqc', 'xxLxonxx']
usernames.clear()
if usernames: # the if is to check if usernames are registered
    for username in usernames:
        if username == 'admin':
            print("Hello Admin would you like to see a status report?")
        else:
            print(f"Hello {username} thank you for logging in again!")
else:
    print("We need to find some users!")


