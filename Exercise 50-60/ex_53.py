"""Python Program to Iterate Over Dictionaries Using for Loop"""

dictionary = {
    "person1":"Jordan",
"person2":"Astrid", "person3":"Lisbeth"}

for k,y in dictionary.items():
    print(k,y)

for key in dictionary:
    print(key,dictionary[key])