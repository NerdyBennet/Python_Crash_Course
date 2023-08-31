#.sort() is permanently
print("Here is the original list:")
cars = ["bmw","audi","toyota","subaro"]
print(cars)
#cars.sort() #sorts alphabetically (ABC)
cars.sort(reverse=True) #sorts reverse alphabetically (ZYX)
print(cars)

#.sorted() ("To maintain the original order of a list but present it in a sorted order")
print("\nHere is the sorted list:")
#print(sorted(cars,reverse=True)) #temporarily reverse sorted list (ZYX)
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

#printing a list in reverse order
cars.reverse() #reverses the order of the list (permanent)
print("\n")
print(cars)
cars.reverse()
print(cars)
print("\n")
print(len(cars))