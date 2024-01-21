car_brands = ["audi", "honda", "lamborghini","Porsche","chefrolet"]
print(f"I want to own a {car_brands[2].title()} someday!") # this
# is just an example
print(f"{car_brands[1].title()} sucks.") # and this
# is just an example too
print(f"{car_brands[0].title()} is cool!")

car_brands[1] = "opel"
car_brands.append("bmw") # puts "bmw" at the end of the list
print(car_brands)

example_list = []
example_list.append("1")
example_list.append("2")
example_list.append("3")
print(example_list)
example_list.insert(0, "7") # 7 gets moved to the 0.(1.)index
print(example_list)
del example_list[0] # del = delete
print(example_list)

"""The pop() method removes the last item in a list, but it lets you
work with that item after removing it.The term pop comes from thinking
of a list as a stack
of items and popping one item off the top of the stack.
"""
popped_car_brands = car_brands.pop() 
print(car_brands)
print(popped_car_brands)

car_brands.remove("chefrolet") # deletes an object by its value
print(car_brands)

del car_brands[-1] # deletes the last item of a list 
# -2 second item from the end of the list
# -3 returns the third item from the end, and so forth
print(car_brands)

# remove an element with a reason
too_expensive = ("lamborghini")
car_brands.remove(too_expensive)
print(car_brands)
print(f"\n\tA {too_expensive.title()} is too expensive for me.") 
# \n = new line
# \t = tab


