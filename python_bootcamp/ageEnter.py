def main():
    pass

if __name__ == '__main__':
    main()
def ask_age():
    age = int(input("Please enter your age: "))

    if age <= 12:
        print("Kid")
    elif age <= 19:
        print("Teenager")
    elif age <= 30:
        print("Young Adult")
    elif age <= 64:
        print("Adult")
    elif age == 65:
        print("Senior")
    elif age >= 66:
        print("Old Fucker")
    else:
        print("WTF")
ask_age()
