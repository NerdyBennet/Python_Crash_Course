pywords = {
    'loop': 'a programming structure that repeats instructions',
    'list': 'yeah basically a list in which you can store data',
    'tuple': 'a kind of list with immutable elements in it',
    'string': 'a sequence of characters',
    'boolean': 'true or false'
}

for words in pywords: # words = key
    meaning = pywords[words] # meaning = value  
    print(f"{words.title()}: {meaning}\n")