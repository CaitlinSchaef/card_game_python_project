import random 
# python my_script.py
# this is A card, a singular card
# build a dictionary of suits and values
# python 'none' = js 'null'
suits = [
    'Diamonds',
    'Hearts', 
    'Spades',
    'Clubs'
]
# cards start at 2, not 0, so making the indexes line up, but Ace can be 0 or 1
values = [
    2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace'
]

class Card: 
    # this initializes the variables 
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
#the above does print the suit and values

# this_is_the_card_i_am_creating_it_is_a_new_and_unique_snowflake = Card('heart', 9)
# gives us heart
# print(f'{this_is_the_card_i_am_creating_it_is_a_new_and_unique_snowflake.suit} {this_is_the_card_i_am_creating_it_is_a_new_and_unique_snowflake.values}')
# gives us heart 9

#class is a special function that makes objects, and automatically returns a new one, the init part is the constructor that says what happens when we make a new one 
class Deck:
    def __init__(self):
        self.list_of_cards = [Card(suit, value) for suit in suits for value in values]

#this is also not a part of the Deck class dummy
#new deck has a property in it called list of cards, so new_deck.list_of_cards is the array 
new_deck = Deck()
for card in new_deck.list_of_cards: 
    # this is just a loop to look at them, and it does produce all of the lines
    print(card.value, 'of'  ,card.suit)

#this is not part of the Deck class
def deck_number():
    deck_choice = input('How many decks do you want to use? (# < 6)')
    if (input < 1 or input > 6 ):
        print('No dice you big dumb baby')
        deck_number()
        #putting deck_number() after this if statement runs it again to ask the question 
    else:
        return [Deck() for num in range(deck_choice)]



# the inits inside of the class are the constructors for the class, so when we do Player(), it's running the init function there 
class Player:
    def __init__(self):
        self.player_name = input('What is your name?')
        self.hand = []
        self.wins = 0


class Game:
    def __init__(self):
        self.player = Player()
        self.decks = deck_number()
        random.shuffle(self.decks)
        self.dealer_hand = []
        self.dealer_wins = 0
    
    #we're not dealing in the init, we're dealing in the deal function
    def deal(self):
        self.player.hand = self.decks.pop(0)
        self.dealer_hand = self.decks.pop(0)
        print(f'Player Card: {self.player.hand.value} of {self.player.hand.suit}')
        print(f'Player Card: {self.dealer_hand.value} of {self.dealer_hand.suit}')
    

    # def check_win:
        

# def shuffle
    # shuffle first
    # maybe make something print thats like: hit enter to shuffle deck 
    # it will be like: shuffled = random.shuffle(new_deck.list_of_cards) [need to put 'import random' somewhere to use the random.shuffle]
    # if two decks, add them together before the shuffle? Will i need to make a double function? I'd rather make one function where the parameter switched based on their answer 
#def deal cards:
    # give dealer one card, give player one card 
    # delete from 'shuffled'

# weight the cards value
    #compare the values of the two cards, if one value is greater than the other, declare winner, if other card 

#declare winner 
#class Dealer:
#dealer gets a card

Game()