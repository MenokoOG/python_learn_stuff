def hello_name():
    n: str = input("Enter your first name with \nno spaces before or after:")
    print("Your Name down the page: ")
    """to get name down page"""
    for let in n:
        print(let)
    print("Your name is: " + n)

    def my_name_count():
        count_n = n
        """to get letter count in name input"""
        print("The number of letters in your name is: " + str(len(count_n)))

    my_name_count()


hello_name()

# nested functions
# def function1():  # outer function
#     print("Hello from outer function")
#
#     def function2():  # inner function
#         print("Hello from inner function")
#
#     function2()
#
#
# function1()
print("-----------------------------")
