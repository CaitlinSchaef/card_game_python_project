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
        # print(self.value)
        # print(self.suit)
    
    
    # lets make a produce card method -this is legit broken
    # def make_cards(self):
    #     self.suit[0] = diamonds
    #     diamonds = self.values.slice('') + "of Diamonds"
# this_is_the_card_i_am_creating_it_is_a_new_and_unique_snowflake = Card('heart', 9)

# print(f'{this_is_the_card_i_am_creating_it_is_a_new_and_unique_snowflake.suit} {this_is_the_card_i_am_creating_it_is_a_new_and_unique_snowflake.values}')
# #gives us heart

#class is a special function that makes objects, and automatically returns a new one, the init part is the constructor that says what happens when we make a new one 
class Deck:
    def __init__(self):
        self.list_of_cards = [Card(suit, value) for suit in suits for value in values]
#new deck has a property in it called list of cards, so new_deck.list_of_cards is the array 
new_deck = Deck()
for card in new_deck.list_of_cards: 
    # this is just a loop to look at them, and it does produce all of the lines
    print(card.value, 'of'  ,card.suit)

    def deck_number(self):

    def shuffle(self):

        #you need to set the deck number first, because if the player selects more than one deck, in the shuffle you need to add the decks together before you shuffle



# class Player:
# player = input('What's your name?)

#class Game: 
# weight the cards value

#declare winner 
#class Dealer:
#dealer gets a card