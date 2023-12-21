#simply, containers are objects that contain other objects. This is an overview of containers.
#in python, everything is an object, even the simplest strings and numbers are consindered objects.



x = "My favorite number is"
y = 21
print(x, y)
#containers(also called collections) are objects that contain objects.
#in this example, the fruits variable contains three strings. remember, all are objects.
fruits = ["bananas", "apples", "grapes"]
print(fruits)


#python lists, a python list is an oredered container, syntax is such
pets = ["dog", "cat", "rabbit"] #create list using brackets []
print(pets)
#a list can caontain mixed data types
x = ["dog", 21, True]
print(x)
#Indexing, is used to access the items of a list. Indexing uses square and numbers 
# to access individual items of a list, 0 refers to the first item, 1 refers to the second item, and so on
pets = ["dog", "cat", "rabbit"]
print(pets[0])
print(pets[1])
print(pets[2])
#negative indexing, is used to access the items of a list using negative numbers, -1 refers to the last item of a list, 
# -2 refers to the second to last item
pets = ["dog", "cat", "rabbit"]
print(pets[-1])
print(pets[-2])
print(pets[-3])
#range of indexes, using a : we can access a range of items at once, the first index is the start of range, 
# while the second index is the end of the range(not included)
pets = ["dog", "cat", "rabbit", "fish", "hamster"]
x = pets[1:3] # ['cat', 'rabbit']
print(x)
#if yo do not specify a start, the range starts at index 0, 
pets = ["dog", "cat", "rabbit", "fish", "hamster"]
x = pets[:3] 
print(x)
# alternately if you do not specify a last index, the range ends with the last tiem of list.
pets = ["dog", "cat", "rabbit", "fish", "hamster"]
x = pets[1:]
print(x)
#adding items to a list with append(), insert(), del keyword
#append() method adds an item to hte end of a list.
pets = ["dog", "cat"]
pets.append("rabbit")
print(pets)
#insert() method inserts an item at the specified index.
pets = ["dogs", "cat", "fish"]
pets.insert(0, "rabbit")
pets.insert(2, "hamster")
print(pets)
print(pets[0])
print(pets[2])
#deleting items from he list, uses pop(), remove()
#the pop() method removes the last item from a list
pets = ["dog", "cat", "rabbit"]
pets.pop()
print(pets)
#the remove() method removes the specified item value.
pets = ["dog", "cat", "rabbit"]
pets.remove("cat")
print(pets)
# del keyword delets a specified index
pets = ["dog", "cat", "rabbit"]
del pets[2]
print(pets)
#the len() method is used to get the length or number of items in a list
pets = ["dog", "cat", "rabbit"]
print(len(pets))
#changing an item's value, access the index fairst and use the assignment operator
pets = ["dog", "cat", "rabbit"]
pets[2] = "fish"
print(pets)
goodGuns = ["ak-47", "M-16", "AR-15"]
print(goodGuns)
goodGuns[1] = "Bazooka"
print(goodGuns)
# use in operator to check if an item exits, returns True if item if found, otherwise False
pets = ["dog", "cat", "rabbit"]
print("dog" in pets)
print("python" in pets)
#extend() method, adds all items from a list to another list,
nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
nums1.extend(nums2)
print(nums1)
#Looping through a list, basically means assessing all its items or elements one-by-one, the for loop is used to loop through
#a list
pets = ["dog", "cat", "rabbit"]
for pet in pets:
    print(pet)
goodGuns = ["ak-47", "M-16", "AR-15"]
for gun in goodGuns:
    print(gun)
#another way to create a list, the way above was called literal, another way is to use the list() constructor.
pets = list(("dog", "cat", "rabbit"))
print(pets)