name = "olaf peter"
print(name.title()) # title() puts the first letter of the words assosiated with it in capital
print(name.upper())
print(name.lower())

first_name = "olaf"
last_name = "peter"
full_name = f"{first_name} {last_name}" # f-string (f stands for format)
message = (f"Hello, {full_name.title()}!")
print(message)

print("\tname") # tab output
print("names that came to mind spontaneously: \n\tAlfred\n\tAlberto\nRoberto\n\tLars") #new line(Zeilenumbruch) you can't do \t\n bc it wont make sense

name_with_spaces = " Sah ra " # name mit Leerzeichen links sowie rechts
print(name_with_spaces.strip()) # only temporary stripes both left and right' Sah rah '
# print(name_mit_space.rstrip()) stripes spaces of the right site (also temporary)
# print(name_mit_space.lstrip()) stripes spaces of the left site (also temporary)
# if you want to strip the value of a variable permanently you have to change the value manually w
name_with_spaces = name_with_spaces.strip()
print(name_with_spaces) # now with out spaces


