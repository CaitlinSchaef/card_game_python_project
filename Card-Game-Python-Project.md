## Logic:
## Cards:
Make two variables that have lists assigned to them, one being value and one being suits
Then to make cards add each element of the value array to each of the suits
Those are your cards that make up the deck

## Deck:
Holds the cards, basically I think you just need to assign it a numeric value, so that you can say if you want to play with 1 or 2 decks (or more)
Should the shuffle function be in this class?

## Players
Signifies the number of players
Default 2 players, one is the computer/terminal and the other is the user
So I guess in theory you could name them: 'Dealer' & 'Player' 
OR if you didn't want the temrinal to play you could assign 'Player 1' & 'Player 2' and have people play against eachother
If Dealer + Player, assign an input to Player value for the terminal to take someone's name


## Game Play:
1. One object removed from deck and given to dealer, and one object removed from deck and given to player
    -make a player card display?
2. Values of cards are weighed against each other
    -If one number value is greater, that player wins
    -Else If tie of value, suit can break
    -If number of decks is 2, then there really can be a tie, if the exact same cards are pulled


## The actual print in the terminal flow:
Should be something like:
    - What is your name?
    - Let's play!
    -Two decks? (Yes/No)
    -Hit enter to shuffle deck!
    -Deck shuffled!
    -Hit enter to deal!
    -Display player card
    -Say if player or dealer won
        ''Name' won!' or 'Dealer won!'
    -Play again?(Yes/No)
        -If yes, ask: Shuffle deck or continue play?
            -If shuffle deck, run shuffle and restart
            -If continue play, just keep dealing from the same deck.
        -If no, print: Game over!