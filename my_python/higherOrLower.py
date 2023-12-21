""" Card game called higher or lower project. Eight cards are randomly chosen from a deck. First card shown is face up. The game asks the player to predict wheter the next card in the selection will have higher or lower value than the current showing card. If the player guesses correctly, they get 20 points. If they choose incorrectly, the lose 15 points. If the next card to be turned over has the same value as the previous card, the player is incorrect. Love that right? Maybe change logic for that to where player gets the win?"""

#HigherOrLower

import random

#card constants
SUIT_TUPLE = ('Spades', 'Hearts', 'Clubs', 'Diamonds')
RANK_TUPLE = ('Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King')

NCARDS = 8


def getCard(deckListIn):
    """Pass in a deck and this function returns a random card from the deck. """
    thisCard = deckListIn.pop()
    return thisCard #pop one off the top of the deck and return


def shuffle(deckListIn):
    """Pass in a deck and this function returns a shuffled copy of the deck. """
    deckListOut = deckListIn.copy() # make a copy of the starting deck
    random.shuffle(deckListOut)
    return deckListOut

#Main Code
print('Welcome to Higher or Lower ')
print()
print('You have to choose whether the next card to be shown will be higher or lower the the current card.')
print()
print('Getting it right adds 20 points; get it wrong and you lose 15 points.')
print()

startingDeckList = []

for suit in SUIT_TUPLE:
    for thisValue, rank in enumerate(RANK_TUPLE):
        cardDict = {'rank':rank, "suit":suit, 'value':thisValue + 1}
        startingDeckList.append(cardDict)
score = 50

while True: 
    """play multiple games"""
    print()
    gameDeckList = shuffle(startingDeckList)
    currentCardDict = getCard(gameDeckList)
    currentCardRank = currentCardDict['rank']
    currentCardValue = currentCardDict["value"]
    currentCardSuit = currentCardDict['suit']
    print('Starting card is: {} of {}'.format(currentCardRank, currentCardSuit))
    print()
    
    for cardNumber in range(0, NCARDS):
        """play one game of this many cards."""
        answer = input('Will the next card be higher or lower than the {} of {} ? (enter h or 1):'.format(currentCardRank, currentCardSuit) )
        answer = answer.casefold()
        """force lowercase"""
        nextCardDict = getCard(gameDeckList)
        nextCardRank = nextCardDict['rank']
        nextCardSuit = nextCardDict['suit']
        nextCardValue = nextCardDict['value']
        print('Next card is {} of {}'.format(nextCardRank, nextCardSuit))
        
        if answer == 'h':
            if nextCardValue > currentCardValue:
                print('You got it right, it was higher')
                score = score + 20
            else:
                print('Sorry, it was not higher')
                score = score - 15
                
        elif answer == '1':
            if nextCardValue < currentCardValue:
                print('You got it right, it was lower')
                score = score + 20
            else:
                print('Sorry, it was not lower')
                score = score -15
        print('Your score is {}'.format(score))
        print()
        currentCardRank = nextCardRank
        currentCardValue = nextCardValue
        """don't need current suit"""
    goAgain = input('To play agian, press ENTER, or "q" to quit:')
    if goAgain == 'q':
        break
print('Ok bye!')