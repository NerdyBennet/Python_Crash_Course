guests = ["Stan Lee","Morgan","Jim"]
print(f"Hello {guests[0]} would you like to come over for a dinner?")
print(f"Hi {guests[1]} would you like to come over for a dinner?")
print(f"Hey {guests[2]} would you like to come over for a dinner!")

print(f"{guests[2]} sadly can't come.")
guests.remove("Jim")

guests.insert(2, "Robert")

print(f"{guests}")
print(f"Hey {guests[0]} sadly can't come.")
print(f"Hey {guests[1]} sadly can't come.")
print(f"Hey {guests[2]} would you like to come over for a dinner?")
print(f"{guests}")

guests.insert(0, "Hugh")
guests.insert(1, "Arnold")
guests.append("Shaq")

print(f"{guests}")
print(f"Hey {guests[0]} would you like to come over for a dinner?")
print(f"Hey {guests[1]} would you like to come over for a dinner?")
print(f"Hey {guests[5]} would you like to come over for a dinner?")

print(f"{guests}")

print(f"Hey {guests[0]} i've found a bigger table!")
print(f"Hey {guests[1]} i've found a bigger table!")
print(f"Hey {guests[2]} i've found a bigger table!")
print(f"Hey {guests[3]} i've found a bigger table!")
print(f"Hey {guests[4]} i've found a bigger table!")
print(f"Hey {guests[5]} i've found a bigger table!")

print(f"{guests}")

print("The table isn't arriving on time so I can only invite 2 people.")
poped_guests1 = guests.pop()
print(f"Sorry " + poped_guests1 + " I can only invite 2 people and have to withdraw my invitation.")
poped_guests2 = guests.pop()
print(f"Sorry " + poped_guests2 + " I can only invite 2 people and have to withdraw my invitation.")
poped_guests3 = guests.pop()
print(f"Sorry " + poped_guests3 + " I can only invite 2 people and have to withdraw my invitation.")
poped_guests4 = guests.pop()
print(f"Sorry " + poped_guests4 + " I can only invite 2 people and have to withdraw my invitation.")
print(f"{guests}")

print(f"Hey {guests[0]} you are still invited!")
print(f"Hey {guests[1]} you are still invited!")
print(len(guests))

del guests[0] 
del guests[0]

print(f"{guests}")

