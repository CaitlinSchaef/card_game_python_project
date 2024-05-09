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



# the inits inside of the class are the constructors for the class, so when we do Player(), it's running the init function there, but it won't run unless Player is called
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
        if self.player.hand.value == 'Jack':
            self.player.hand.value = 11
        elif self.player.hand.value == 'Queen':
            self.player.hand.value = 12
        elif self.player.hand.value == 'King':
            self.player.hand.value = 13
        elif self.player.hand.value == 'Ace':
            self.player.hand.value = 14
        elif self.dealer_hand.value == 'Jack':
            self.dealer_hand.value = 11
        elif self.dealer_hand.value == 'Queen':
            self.dealer_hand.value = 12
        elif self.dealer_hand.value == 'King':
            self.dealer_hand.value = 13
        elif self.dealer_hand.value == 'Ace':
            self.dealer_hand.value = 14
        else:
            return 
        
    def check_suit_values(self):
        if self.player.hand.suit == 'Diamonds':
            self.player.hand.suit = 2
        elif self.player.hand.suit == 'Hearts':
            self.player.hand.suit = 3
        elif self.player.hand.suit == 'Spades':
            self.player.hand.suit = 4
        elif self.player.hand.suit == 'Clubs':
            self.player.hand.suit = 1
        elif self.dealer_hand.suit == 'Diamonds':
            self.dealer_hand.suit = 2
        elif self.dealer_hand.suit == 'Hearts':
            self.dealer_hand.suit = 3
        elif self.dealer_hand.suit == 'Spades':
            self.dealer_hand.suit = 4
        elif self.dealer_hand.suit == 'Clubs':
            self.dealer_hand.suit = 1
        else:
            return 

    #def i_am_a_function_that_returns_a_number_based_on_the_self_player_hand(self, value):
        # if (value == 'Jack')
    def check_win(self):
        self.face_values()
        # print(f'player hand value: {self.player.hand.value}')
        # print(f'dealer hand value: {self.dealer_hand.value}')
        # print(f'new player card value: {self.player.hand.value} of {self.player.hand.suit}')
        # print(f'new dealer card value: {self.dealer_hand.value} of {self.dealer_hand.suit}')
        if self.player.hand.value > self.dealer_hand.value:
            print(f'{self.player.player_name} won!')
            self.player.wins = self.player.wins + 1
        elif self.player.hand.value < self.dealer_hand.value:
            print('Dealer won!')
            self.dealer_wins = self.dealer_wins + 1
        elif self.player.hand.value == self.dealer_hand.value:
            self.check_suit_values()
            if self.player.hand.suit > self.dealer_hand.suit:
                print(f'{self.player.player_name} won!')
                self.player.wins = self.player.wins + 1
            elif self.player.hand.suit < self.dealer_hand.suit:
                print('Dealer won!')
                self.dealer_wins = self.dealer_wins + 1
        else:
            print('I am sad that I got here.')
    

    def check_continue(self):
        main_question = input(f'Do you want to keep playing {self.player.player_name}? (Yes/No)')
        if main_question == "No" or main_question == "no":
            print('Game over!')
        else:
            print('Great!')
            second_question = input(f'Continue with same deck or new deck? (new deck/same deck)')
            if second_question == "new deck":
                new_deck = Deck()
                self.deal()
                self.check_win()
                print(f'{self.player.player_name} Wins: {self.player.wins}')
                print(f'Dealer Wins: {self.dealer_wins}')
            elif second_question == "same deck":
                self.deal()
                self.check_win()
                print(f'{self.player.player_name} Wins: {self.player.wins}')
                print(f'Dealer Wins: {self.dealer_wins}')
       


#This is the actual flow of the game, because it is what is calling all of the other functions in the init
    def __init__(self):
        print("Let's play!")
        self.player = Player()
        self.decks = deck_number()
        #below this the random.shuffle shuffles the deck based on the number of decks the player provides
        random.shuffle(self.decks)
        # print(self.decks)
        self.dealer_hand = []
        self.dealer_wins = 0
        self.deal()
        self.check_win()
        print(f'{self.player.player_name} Wins: {self.player.wins}')
        print(f'Dealer Wins: {self.dealer_wins}')
        self.check_continue()
    # def check_win:
    # weight the cards value
        #compare the values of the two cards, if one value is greater than the other, declare winner, if other card 

Game()