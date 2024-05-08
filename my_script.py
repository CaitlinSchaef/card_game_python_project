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
    # cards start at 2, not 0, so making the indexes line up 
    values = [
        None, None, '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace'
    ]

    # this initializes the variables 
    def __init__(self, suit, values):
        self.suit = suit
        self.values = values
    
    # lets make a produce card method -this is legit broken
    def cards(self, diamonds, values):
        if (self.suit == "Diamond"):
          diamonds = map(self.values, + "of Diamonds")
          return diamonds
        elif (self.suit == "Hearts"):
            hearts = self.values + "of Hearts"
            return hearts
        elif (self.suit == "Spades"):
            spades = self.values + "of Spades"
            return spades
        elif (self.suit == "Clubs"):
            clubs = self.values + "of Clubs"
            return clubs
        else:
            return "No card here!"
        


# class Deck:

# class Player:
