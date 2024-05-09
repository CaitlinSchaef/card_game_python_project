import random 
# python my_script.py
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

# this is A card, a singular card
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
# for card in new_deck.list_of_cards: 
    # this is just a loop to look at them, and it does produce all of the lines
    # print(card.value, 'of'  ,card.suit)

#this is not part of the Deck class
def deck_number():
    #wrapping it in int converts it from a string to an integer value
    deck_choice = input('How many decks do you want to use? (# < 6)')
    if deck_choice.isnumeric():
        deck_choice = int(deck_choice) 
    else: 
        print('No dice you big dumb baby!')
        return deck_number()

    if (deck_choice < 1) or (deck_choice > 6):
        print('No dice you big dumb baby!')
        return deck_number()
        #putting deck_number() after this if statement runs it again to ask the question 
    else:
        print(deck_choice)
        # decks = [Deck() for num in range(deck_choice)]
        flat_decks = []
        for _ in range(deck_choice):
            tempDeck = Deck()
            flat_decks.extend(tempDeck.list_of_cards)
        # flat_decks.extend(deck)
        return flat_decks



# the inits inside of the class are the constructors for the class, so when we do Player(), it's running the init function there 
class Player:
    def __init__(self):
        self.player_name = input('What is your name?')
        self.hand = []
        self.wins = 0


class Game:
    #all the class methods that are in this thing need to happen before init because it has to be defined before called

    #we're not dealing in the init, we're dealing in the deal function
    def deal(self):
        # The pop() method removes the element at the specified position.
        self.player.hand = self.decks.pop(0)
        self.dealer_hand = self.decks.pop(0)
        print(f'Player Card: {self.player.hand.value} of {self.player.hand.suit}')
        print(f'Dealer Card: {self.dealer_hand.value} of {self.dealer_hand.suit}')

    def face_values(self):
        if self.player.hand.value == "Jack" or self.dealer_hand.value == "Jack":
            return 11
        elif self.player.hand.value == "Queen" or self.dealer_hand.value == "Queen":
            return 12
        elif self.player.hand.value == "King" or self.dealer_hand.value == "King":
            return 13
        elif self.player.hand.value == "Ace" or self.dealer_hand.value == "Ace":
            return 14
        else:
            return self.value
        
    def check_suit_values(self):
        "Diamonds" > "Hearts" and "Diamonds" > "Spades" and "Diamonds" > "Clubs"
        "Hearts" > "Spades" and "Hearts" > "Clubs"
        "Spades" > "Clubs"


    def check_win(self):
        self.face_values()
        if {self.player.hand.value} > {self.dealer_hand.value}:
            print(f'{self.player_name} won!')
            return self.wins + 1
        elif {self.player.hand.value} < {self.dealer_hand.value}:
            print('Dealer won!')
            return self.dealer_wins + 1
        elif {self.player.hand.value} == {self.dealer_hand.value}:
            self.check_suit_values()

    def __init__(self):
        self.player = Player()
        self.decks = deck_number()
        #below this the random.shuffle shuffles the deck based on the number of decks the player provides
        random.shuffle(self.decks)
        # print(self.decks)
        self.dealer_hand = []
        self.dealer_wins = 0
        self.deal()
        self.check_win()
        print(f'{self.player_name} Wins: {self.wins}')
        print(f'Dealer Wins: {self.dealer_wins}')

    


    # def check_win:
    # weight the cards value
        #compare the values of the two cards, if one value is greater than the other, declare winner, if other card 

Game()