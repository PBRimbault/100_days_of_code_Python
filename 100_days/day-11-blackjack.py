############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.

from random import randint

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    delt_card = cards[randint(0, len(cards) - 1)]
    return delt_card

user_cards = []
dealer_cards = []

i = 0

while i <= 1:
    user_cards.append(deal_card())
    dealer_cards.append(deal_card())
    i += 1

def card_check(user_cards, dealer_cards):
    user_score = user_cards[0] + user_cards[1]
    dealer_score = dealer_cards[0] + dealer_cards[1]

    print(f"User cards: {user_cards} User score: {user_score}")
    print(f"Dealer cards: {dealer_cards} User score: {dealer_score}")

    if user_score == 21 and dealer_score == 21:
        print("The user and the dealer has blackjack. Game drawn")
    elif user_score == 21 and dealer_score == 21:
        print("The user has wone with blackjack.")
    elif dealer_score == 21:
        print("The user has lost, dealer has blackjack")

    if user_score > 21:
        while test_card in user_cards == 11:
            user_cards[test_card] = 1

card_check(user_cards, dealer_cards)