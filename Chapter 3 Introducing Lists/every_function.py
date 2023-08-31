languages = []
languages.append("german") #1
languages.insert(1, "english") #2
languages.append("chinese")
languages.append("dutch")
languages.append("mandarin")
languages.append("french")
languages.append("spanish")
languages.append("hindi")
languages.append("turkish")


print(f"{languages[0].title()}") #3
print(f"{languages[1].title()}")

del languages[1] #4
print(languages)

popped_languages = languages.pop() #5 
print(popped_languages)

languages.remove("chinese") #6
print(languages)

languages.sort() #7 
print(languages)

languages.sort(reverse=True) #8
print(languages)

print(sorted(languages)) #9

print(sorted(languages, reverse=True)) #10

languages.sort()
print(languages)

languages.reverse() #11
print(languages)

print(len(languages)) #12

