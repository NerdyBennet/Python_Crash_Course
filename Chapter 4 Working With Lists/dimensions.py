"""
tuples are simple data structures that are used for values that
shouldn't be changed throughout the life of a program
"""

dimensions = (200, 50) # parentheses instead of square brackets
print(dimensions[0])
print(dimensions[1])

# if you want to make a tuple with one element you need a comma
# my_t = (3,)

print("Original dimensions:")
# loop through a tuple
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100) 
# you can't technically modify a tuple you can only overwrite it
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)