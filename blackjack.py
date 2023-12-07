import random

#list of cards
Cards = ["A♠", "2♠", "3♠", "4♠", "5♠", "6♠", "7♠", "8♠", "9♠", "10♠", "J♠", "Q♠", "K♠",
         "A♥", "2♥", "3♥", "4♥", "5♥", "6♥", "7♥", "8♥", "9♥", "10♥", "J♥", "Q♥", "K♥", 
         "A♣", "2♣", "3♣", "4♣", "5♣", "6♣", "7♣", "8♣", "9♣", "10♣", "J♣", "Q♣", "K♣", 
         "A♦", "2♦", "3♦", "4♦", "5♦", "6♦", "7♦", "8♦", "9♦", "10♦", "J♦", "Q♦", "K♦"]

#initializing dealer and player cards variables 
dealer_cards = ""
player_cards = ""
player_cards1 = ""

#game flow 
def gameMain():
    valueCalc()
    playerMove()

#performs program based on player's input/move
def playerMove():
    move = input("What's the move?(Hit/Stand/Double) --> ")
    if move == stand:
        stand()
    
    elif move == hit:
        player_cards += random.choice(Cards)
    
    elif move == double:
        player_cards1 = player_cards + random.choice(Cards)

def valueCalc():
#    if dealer_cards == 
#        print(f"dealer: {}")
    



    


    