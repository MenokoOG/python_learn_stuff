#Membership operators are used to check if a sequence is present in an object like strings, lists, etc
# there are two membership operators, in, not in, the in operators returns True is a sequence or 
#value is present in an object, 
txt = "luv python programming"
print("love" in txt) #False
print("luv" in txt)
#here is an example using a list
fruits = ["bananas", "apple", "grape"]
print("grapes" in fruits) #False becasue grapes is not grape with the object.
print("lemons" in fruits)
print("grape" in fruits)
#the not in operator returns True if a sequence or value is not present in an object.
txt = "I luv fruits"
print("veges" not in txt)
print("luv" not in txt)
fruits = ["bananas", "apple", "grape"]
print("grapes" not in fruits) #False becasue grapes is not grape with the object.
print("lemons" not in fruits)
print("grape" not in fruits)