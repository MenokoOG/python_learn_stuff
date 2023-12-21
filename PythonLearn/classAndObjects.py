#in python everything is an object, a class helps us create objects. use the class keyword to create a class



class Person:
    first_name = "Killer"
    last_name = "MacDaddy"
    age = 50
#now we can create an object from that class by instantiating it, to instantiate a class, add round brackets () to its class name
obj = Person()
print(obj.first_name)
print(obj.last_name)
print(obj.age)
#classes can have attributes, in the next example the Student class can have attributtes like id_number, name, and age.
class Student:
    def __init__(self, id_number, name, age):
        self.id_number = id_number
        self.name = name
        self.age = age
student1 = Student(1234, "John Doe", 103)
x = student1.id_number
y = student1.name
z = student1.age
print("Student ID", x)
print("student Name:", y)
print("Student Age:", z)
#student1 is a unique instance of the Student class, so an instance is simply the object from a class. 
# values can be passed the properties of the instance.
# the self parameter allows us to access the attributes and methods of a class. the _init_() function allows us to 
# provide values for the attributes of a class. bring the class to life so to speak to be used agian if needed.
# once a class is established then a child can be created form the parent object along with attirbutess and then 
# another class can be created and share attributtes from the two now.
class Student:
    def __init__(self, id_number, name, age):
        self.id_number = id_number
        self.name = name
        self.age = age
student1 = Student(2435, "Mary Doe", 18)
student2 = Student(3221, "Joker Doe", 19)
print("Student 1 ID:", student1.id_number)
print("Student 1 Name:", student1.name)
print("Student 1 Age:", student1.age)

print("--------------------------")

print("Student 2 ID:", student2.id_number)
print("Student 2 Name:", student2.name)
print("Student 2 Age:", student2.age)
