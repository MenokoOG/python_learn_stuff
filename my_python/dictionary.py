#dictionary is an undordered and mutable colletion of items, it is written using {} 
# each item in a dictionary contains a key/value pair.
person = {
    "first_name": "Jazzy",
    "last_name": "Smith",
    "age": 30
}
print(person)
#to access an item, specify the key name of an item inside []
person = {
    "first_name": "Jazzy",
    "last_name": "Smith",
    "age": 30
}
x = person["first_name"]
y = person["last_name"]
z = person["age"]
print("First Name:", x)
print("Last Name:", y)
print("Age:", z)
#if you acces an item using a key that does not exist, an error will occur, 
# instead use get()
person = {
    "first_name": "Jazzy",
    "last_name": "Smith",
    "age": 30
}
print(person.get("first_name"))
#add an item, specify a new index key name inside [] brackets and assign a value using the assignment operator.
person = {
    "first_name": "Jazzy",
    "last_name": "Smith",
    "age": 30
}
person["hobby"] = "playing games"
print(person)
#to remove an item us the pop() method, the method removes an item with the specified key name.
person = {
    "first_name": "Jazzy",
    "last_name": "Smith",
    "age": 30
}
person.pop("age")
print(person)
#anotehr way is to use the del key word
person = {
    "first_name": "Jazzy",
    "last_name": "Smith",
    "age": 30
}
del person["age"]
print(person)
#get length of dictionary
person = {
    "first_name": "Jazzy",
    "last_name": "Smith",
    "age": 30
}
print(len(person))
#check if an item exits usinf if statement
person = {
    "first_name": "Jazzy",
    "last_name": "Smith",
    "age": 30
}
if "age" in person:
    print('the "age" key exits')
#loop through dictionary
person = {
    "first_name": "Jazzy",
    "last_name": "Smith",
    "age": 30
}
for key in person:
    print(person[key])
#Nested dictionary, dictionary can contain another dictionary.
employees = {
    "manager": {
        "name": "Jane Doe",
        "age": 30
    },
    "programmer": {
    "name": "Joe Doe",
    "age": 29
    }
}
print(employees)
#to access an item in a nested dictionary, access the key name of the dictionary then the key name of the item.
employees = {
    "manager": {
        "name": "Jane Doe",
        "age": 30
    },
    "programmer": {
    "name": "Joe Doe",
    "age": 29
    }
}
print(employees["manager"]["name"])
print(employees["programmer"]["name"])