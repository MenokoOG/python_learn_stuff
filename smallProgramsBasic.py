def my_print_line():
    print("-----------------------------------")


# square root
number = int(input("enter a number: "))
sqrt = number ** 0.5
print(("square root: ", sqrt))

my_print_line()


# cube root of a number
def cube_root(x):
    return x ** (1 / 3)


print(cube_root(27))

my_print_line()

# fahrenheit to celsius
temp = float(input("Enter temperature in Fahrenheit: "))
celsius = (temp - 32) * 5 / 9
print(f"{temp} in Fahrenheit is equal to {celsius} in Celsius")

my_print_line()
# celsius to fahrenheit
temp = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 1.8) + 32
print(f"{temp} in Celsius is equal to {fahrenheit} in fahrenheit")

my_print_line()
# area of triangle
Hieght = float(input("Enter Height: "))
Base = float(input("Enter Base: "))
ans = (0.5) * Hieght * Base
print("Area of Triangle", ans)

my_print_line()


