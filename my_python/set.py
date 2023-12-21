#Set is a caontainer(collection) that is unordered and immutable. create using {}
pets = {"dog", "cat", "rabbit"}
print(pets)
#accessing items
for pet in pets:
    print(pet)
#alternative way to create set
pets = set(("dog", "cat", "rabbit"))
print(pets)
#add items
pets = {"dog", "cat", "rabbit"}
pets.add("fish")
print(pets)
#changing an item SET ITEMS CANNOT BE CHANGED
# to remove an item use remove()
pets = {"dog", "cat", "rabbit"}
pets.remove("rabbit")
print(pets)
#difference between remove() and discard() method is discard will not raise 
# errors if the specified item is not present.
pets = {"dog", "cat", "rabbit"}
pets.discard("rabbit")
print(pets)
#pop() method(funtion) can be used, but we cannot determine which item will be removed.
pets = {"dog", "cat", "rabbit"}
pets.pop()
print(pets)
#get length use len() method
pets = {"dog", "cat", "rabbit"}
print(len(pets))
#check to see if tiem exits
pets = {"dog", "cat", "rabbit"}
print("dog" in pets)
print("python" in pets)
#Combine two sets
x = {1, 2, 3}
y = {4, 5, 6}
x.update(y)
print(x)
#difference of two sets, use the - operator
x = {1, 2, 3, 4}
y = {3, 4, 5, 6}
print("x - y:", x - y)
print("y - x:", y - x)
