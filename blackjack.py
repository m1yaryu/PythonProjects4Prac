import random

#list of cards
Cards = ["A♠", "2♠", "3♠", "4♠", "5♠", "6♠", "7♠", "8♠", "9♠", "10♠", "J♠", "Q♠", "K♠",
         "A♥", "2♥", "3♥", "4♥", "5♥", "6♥", "7♥", "8♥", "9♥", "10♥", "J♥", "Q♥", "K♥", 
         "A♣", "2♣", "3♣", "4♣", "5♣", "6♣", "7♣", "8♣", "9♣", "10♣", "J♣", "Q♣", "K♣", 
         "A♦", "2♦", "3♦", "4♦", "5♦", "6♦", "7♦", "8♦", "9♦", "10♦", "J♦", "Q♦", "K♦"]

#initializing dealer and player cards variables 
player_cards = []
dealer_cards = []
dealer_cards1 = []
##start_game = input("Start game?[Y/N] -> ")

#game flow 
def gameMain():
    while start_game == True:
        player_cards.append(random.sample(Cards, 2))
        dealer_cards.append(random.choice(Cards))
        dealer_cards1.append(random.choice(Cards))
        valueCalc()
        print(player_cards)
        playerMove()


#performs program based on player's input/move
def playerMove():
    move = input("What's the move?(Hit/Stand) --> ")
    while move == True:
        if move == stand:
            move == False
    
        elif move == hit:
            player_cards += random.choice(Cards)
    

##def valueCalc():
##    if dealer_cards == 
##        print(f"dealer: {}")

player_cards.append(random.sample(Cards, 2))
dealer_cards.append(random.choice(Cards))
dealer_cards1.append(random.choice(Cards))




print(f"dealer's hand: {' '.join(dealer_cards)} + x")
print(f"your hand: {' '.join(player_cards[0])}")