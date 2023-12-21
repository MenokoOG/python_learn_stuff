#the tuple is an ordered container, same as lists but the items or elements of tuples cannot be changed.
#create a tuple using rounds brackets (), objects placed inside are separated by comma,
pets = ("dog", "cat", "rabbit")
print(pets)
#another wat to create tuple
pets = tuple(("dog", "cat", "rabbit"))
print(pets)
for pet in pets:
    print(pet)
#tuple can contain mixed data
x = ("dog", 21, True)
print(x)
#index a tuple using square brackets [], 0 refers to first item and 1 refers to second item
pets = ("dog", "cat", "rabbit")
print(pets[0])
print(pets[1])
print(pets[2])
#negative indexing is used to access the items of a tuple using negative numbers, -1 refers to last itme and 
# -2 refers to the second to the last item, and so on
pets = ("dog", "cat", "rabbit")
print(pets[-1])
print(pets[-2])
print(pets[-3])
#range of indexes, using a colon :, we can access a range of itmes at once, the first index is start of range and second 
# index is end of range (not included)
pets = ("dog", "cat", "rabbit", "fish", "hamster")
x = pets[1:3] #(''cat', 'rabbit')
print(x)
pets = ("dog", "cat", "rabbit", "fish", "hamster")
x = pets[:2]
print(x)
pets = ("dog", "cat", "rabbit", "fish", "hamster")
x = pets[2:]
print(x)
pets = ("dog", "cat", "rabbit")
print(len(pets))
#loop through a tuple
pets = ("dog", "cat", "rabbit")
for pet in pets:
    print(pet)
pets = ("dog", "cat", "rabbit", "fish", "hamster")
print("dog" in pets)
print("tuna" in pets)
print("hamster" in pets)
guns1 = ("ak47", "9mm", "m16", "ar15")
guns2 = ("bazooka", "panzerhaust", "357 mag")
all_guns = guns1 + guns2
print(all_guns)
for gun in all_guns:
    print(gun)
