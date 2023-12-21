"""Bagels, by Al Sweigart and reproduced for programming project by Lawrence Jefferson II, Menoko OG 2023"""

import random

NUM_DIGITS = 3
MAX_GUESSES = 10


def main():
    print('''Bagels, a deductive logic game for my project
April 2023
          
I am thinking of a {} -digit number with no repeated digits.
Try to guess what it is. Here are some clues:
 When I say:
Pico    One digit is correct but in the wrong position
Fermi   One is correct and in the right position.
Bagels  No digit is correct.

For example, if the secret number was 248 and your guess was 843, the clues would be Fermi Pico'''.format(NUM_DIGITS))

    while True:  # Main game loop
        # this stores the secret number player needs to guess:
        secretNum = getSecretNum()
        print("I have thought up a number.")
        print(" You have {} guesses to get it".format(MAX_GUESSES))

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ""
            # keep looping until they enter a vaild guesss:
            while len(guess) != NUM_DIGITS or not guess:
                print("Guess # {}: ".format(numGuesses))
                guess = input("> ")

            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break  # they're correct, so break out of this loop
            if numGuesses > MAX_GUESSES:
                print("You ran out of guesses.")
                print("The answer was {}.".format(secretNum))
        # ask player if they want to play agian.
        print("Do you want to play agian? (yes or no)")
        if not input (" >").lower().startswith("y"):
            break
    
    print("Thanks for playing!")


def getSecretNum():
    """Returns a string made up of NUM_DIGITS unique random digits."""
    numbers = list("0123456789")  # create a list of digits 0 ot 9
    random.shuffle(numbers)  # shuffle them into random order.

    # get the first NUM_DIGITS digits in the list for secret number:
    secretNum = ""
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum


def getClues(guess, secretNum):
    """Returns a string with the pico, fermi, bagles clues for a guess and secret number pair"""
    if guess == secretNum:
        return "You got it!"

    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            # a correct figit is in the correct place.
            clues.append("Fermi")
        elif guess[i] in secretNum:
            # a correct digit is in theincorrect place.
            clues.append("Pico")
    if len(clues) == 0:
        return "Bagles"  # no correct digits at all.
    else:
        clues.sort()
        return " ".join(clues)


# if the program is run (instead of imported), run the game:
if __name__ == "__main__":
    main()
