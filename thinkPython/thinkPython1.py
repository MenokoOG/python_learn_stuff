print("Hello Wolf!")

miles = 26.2
miles = miles * 1.61
mgr = miles
print(mgr)

miles = 26.2
print(miles * 1.61)

first = "throat"
second = "warbler"
print(first + " " + second)
print(type(first))
print(type(second))
def tw():
    print(first + " " + second)

def my_first_fun():
    print(type(first))
    print(type(second))

def cool_shit():
    first = "me"
    second = "my"
    third = first + second
    for letter in third:
        print(letter)
    print(first + " " + second)
    print(len(first))
    print(len(second))
    print(len(third))

my_first_fun()
tw()
cool_shit()

print(first + " " + second)

def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)
print("------------------------------------------------------------")
class Gun:
    def __init__(self, type, assigned, ammo):
        self.type = type
        self.assigned = assigned
        self.ammo = ammo

        
gun1 = Gun("ak-47", "max", 3000)
print("Gun one is:", gun1.type)
print("Assigned :", gun1.assigned)
print("Ammo Count:", gun1.ammo)

#this is where is left off, trying to create weapon array for messing around with.
print("----------------------------------------------------------")
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