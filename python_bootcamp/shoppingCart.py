#!/usr/bin/env python3

# Initial Setup-import nessecary functions
from IPython.display import clear_output


#global list varaible
cart = []

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ACTIONS CODE BLOCK\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# add
def addItem(item):
    clear_output()
    cart.append(item)
    print(f"{item} has been added.")

# remove
def removeItem(item):
    clear_output()
    try:
        cart.remove(item)
        print(f"{item} has been removed.")
    except:
        print("Sorry we could not remove that item")

# show
def showCart():
    clear_output()
    if cart:
        print("Here is your cart: ")
    for item in cart:
        print(f"-{item}")
    else:
        print("Your cart is empty.")

# clear
def clearCart():
    clear_output()
    cart.clear()
    print("Your cart is empty")
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#  \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\MAIN LOOP CODE BLOCK\\\\\\\\\\\\\\\\\
#   \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# Main loop function or Master Loop- loops until user quits
def main():
    done = False

    while not done:
        ans = input("quit/add/remove/show/clear: ").lower()
    
    # BASE CASE
        if ans == "quit":
            print("Thanks for using our program.")
            showCart()
            done = True
        elif ans == "add":
            item = input("What would you like to add?").title()
            addItem(item)
        elif ans == "remove":
            item = input("What would you like to remove?").title()
            removeItem(item)
        elif ans == "show":
            showCart()
        elif ans == "clear":
            clearCart()
        else:
            print("Sorry that was not an option")

main()  #driver code