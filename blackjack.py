import random
import numpy as np

#list of cards
Cards = ["A♠", "2♠", "3♠", "4♠", "5♠", "6♠", "7♠", "8♠", "9♠", "10♠", "J♠", "Q♠", "K♠",
         "A♥", "2♥", "3♥", "4♥", "5♥", "6♥", "7♥", "8♥", "9♥", "10♥", "J♥", "Q♥", "K♥", 
         "A♣", "2♣", "3♣", "4♣", "5♣", "6♣", "7♣", "8♣", "9♣", "10♣", "J♣", "Q♣", "K♣", 
         "A♦", "2♦", "3♦", "4♦", "5♦", "6♦", "7♦", "8♦", "9♦", "10♦", "J♦", "Q♦", "K♦"]

#initializing dealer and player cards variables 
player_cards = []
dealer_cards = []
dealer_cards1 = []
start_game = input("Start game?[Y/N] -> ")

#game flow 
def gameMain():
    while start_game == True:
        player_cards = random.sample(Cards, 2)
        dealer_cards = random.choice(Cards)
        dealer_cards1 = random.choice(Cards)
        playerVal = 0
        dealerVal = 0
        dealerVal1 = 0  
        for Card in player_cards:
            player_card_value = Card[0]
            if player_card_value == "1" or player_card_value == "J" or player_card_value == "Q" or player_card_value == "K":
                playerVal += 10
            elif player_card_value != "1" and player_card_value != "J" and player_card_value != "Q" and player_card_value != "K" and player_card_value != "A":
                player_card_value = int(player_card_value)
                playerVal += player_card_value
            elif player_card_value == "A":
                playerVal += 11

        dealer_card_value = dealer_cards[0]
        if dealer_card_value == "1" or dealer_card_value == "J" or dealer_card_value == "Q" or dealer_card_value == "K":
                dealerVal += 10
        elif dealer_card_value != "1" and dealer_card_value != "J" and dealer_card_value != "Q" and dealer_card_value != "K" and dealer_card_value != "A":
                dealer_card_value = int(dealer_card_value)
                dealerVal += dealer_card_value
        elif dealer_card_value == "A":
                dealerVal += 11

        dealer_card1_value = dealer_cards1[0]
        if dealer_card1_value == "1" or dealer_card1_value == "J" or dealer_card1_value == "Q" or dealer_card1_value == "K":
                dealerVal1 += 10
        elif dealer_card1_value != "1" and dealer_card1_value != "J" and dealer_card1_value != "Q" and dealer_card1_value != "K" and dealer_card1_value != "A":
                dealer_card1_value = int(dealer_card1_value)
                dealerVal1 += dealer_card1_value
        elif dealer_card1_value == "A":
                dealerVal1 += 11


        print(f"dealer's hand: {' '.join(dealer_cards[0])} x")
        print(f"your hand: {' '.join(player_cards[0])}")
        playerMove()


#performs program based on player's input/move
def playerMove():
    move = input("What's the move?(Hit/Stand) --> ")
    while move == True:
        if move == "stand":
            move == False
    
        elif move == "hit":
            player_cards += random.choice(Cards)
    
