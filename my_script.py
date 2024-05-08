# python my_script.py

class Card: 
# build a dictionary of suits and values
# python 'none' = js 'null'
    suit = [
        'Diamonds',
        'Hearts', 
        'Spades',
        'Clubs'
    ]
    # cards start at 2, not 0, so making the indexes line up, but Ace can be 0 or 1
    values = [
        None, None , 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace'
    ]

    # set integer values for face cards
    # face_cards = {
    #     'Jack': 11,
    #     'Queen': 12,
    #     'King': 13,
    #     'Ace': 14
    # }

    # this initializes the variables 
    def __init__(self, suit=suit, values=values):
        self.suit = suit
        self.values = values
    print(values)
    print(suit)
    list_of_cards = []
    # lets make a produce card method -this is legit broken
    # def make_cards(self):
    #     self.suit[0] = diamonds
    #     diamonds = self.values.slice('') + "of Diamonds"
# this_is_the_card_i_am_creating_it_is_a_new_and_unique_snowflake = Card('heart', 9)

# print(f'{this_is_the_card_i_am_creating_it_is_a_new_and_unique_snowflake.suit} {this_is_the_card_i_am_creating_it_is_a_new_and_unique_snowflake.values}')
# #gives us heart
    
class Deck(Card):
    suits = []
    values = []
    list_of_cards = []
    for suit in suits:
        for value in values:
            list_of_cards.append(Card(suit, value))
    for card in list_of_cards:
        print(f'card: {card.suit}{card.number}')
        print('\n')


# class Player:
