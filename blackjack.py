import random

#list of cards
Cards = ["A♠", "2♠", "3♠", "4♠", "5♠", "6♠", "7♠", "8♠", "9♠", "10♠", "J♠", "Q♠", "K♠",
         "A♥", "2♥", "3♥", "4♥", "5♥", "6♥", "7♥", "8♥", "9♥", "10♥", "J♥", "Q♥", "K♥", 
         "A♣", "2♣", "3♣", "4♣", "5♣", "6♣", "7♣", "8♣", "9♣", "10♣", "J♣", "Q♣", "K♣", 
         "A♦", "2♦", "3♦", "4♦", "5♦", "6♦", "7♦", "8♦", "9♦", "10♦", "J♦", "Q♦", "K♦"]

#User input to start the game
#start_game = input("Start game?[Y/N] -> ")

#creating empty list so it can be accessed anywhere in the code

player_cards = []
dealer_cards = []
dealer_cards1 = []
#Initializing each value
playerVal = 0
dealerVal = 0
dealerVal1 = 0

move = "hit"

def playerMove():
    global move
    global playerVal 
    global dealerVal 
    global dealerVal1
    

    while playerVal <= 21:
        
        move = input("What's the move?(Hit/Stand) --> ").lower()   
        if move == "hit":
            player_card_value = player_cards[len(player_cards)-1][0]
            player_cards.append(random.choice(Cards))
            if player_card_value == "1" or player_card_value == "J" or player_card_value == "Q" or player_card_value == "K":
                playerVal += 10
                print(player_cards[len(player_cards)-1])
                print(f"your hand: {' '.join(player_cards)} ({playerVal})") 
                
            elif player_card_value != "1" and player_card_value != "J" and player_card_value != "Q" and player_card_value != "K" and player_card_value != "A":
                player_card_value = int(player_card_value)
                playerVal += player_card_value
                print(player_cards[len(player_cards)-1])
                print(f"your hand: {' '.join(player_cards)} ({playerVal})") 
                
            elif player_card_value == "A":
               playerVal += 11
               print(player_cards[len(player_cards)-1])
               print(f"your hand: {' '.join(player_cards)} ({playerVal})") 
            
            
        elif move == "stand" and playerVal >= 21:
            break
            

        
        else:
            print("Please enter valid keyphrase: hit or stand")    

    return player_cards, playerVal        

#game flow 
##def gameMain():
##    global playerVal 
##    global dealerVal 
##    global dealerVal1
##    while start_game == "Y":
        #Shuffle and dealing of cards
player_cards.extend(random.sample(Cards, 2))
dealer_cards.append(random.choice(Cards))
dealer_cards1.append(random.choice(Cards))
#Calculating the value of player's hand

for Card in player_cards:
    player_card_value = Card[0]
    if player_card_value == "1" or player_card_value == "J" or player_card_value == "Q" or player_card_value == "K":
        playerVal += 10
    elif player_card_value != "1" and player_card_value != "J" and player_card_value != "Q" and player_card_value != "K" and player_card_value != "A":
        player_card_value = int(player_card_value)
        playerVal += player_card_value
    elif player_card_value == "A":
        playerVal += 11

dealer_card_value = dealer_cards[0][0]
if dealer_card_value == "1" or dealer_card_value == "J" or dealer_card_value == "Q" or dealer_card_value == "K":
        dealerVal += 10
elif dealer_card_value != "1" and dealer_card_value != "J" and dealer_card_value != "Q" and dealer_card_value != "K" and dealer_card_value != "A":
        dealer_card_value = int(dealer_card_value)
        dealerVal += dealer_card_value
elif dealer_card_value == "A":
        dealerVal += 11

dealer_card1_value = dealer_cards1[0][0]
if dealer_card1_value == "1" or dealer_card1_value == "J" or dealer_card1_value == "Q" or dealer_card1_value == "K":
        dealerVal1 += 10
elif dealer_card1_value != "1" and dealer_card1_value != "J" and dealer_card1_value != "Q" and dealer_card1_value != "K" and dealer_card1_value != "A":
        dealer_card1_value = int(dealer_card1_value)
        dealerVal1 += dealer_card1_value
elif dealer_card1_value == "A":
        dealerVal1 += 11

Dealer_Value = dealerVal + dealerVal1

#Output each hand and it's value
print(f"dealer's hand: {''.join(dealer_cards)} x ({dealerVal})")
print(f"your hand: {' '.join(player_cards)} ({playerVal})")

playerMove()


###if playerVal == 21:
###     print("You win!")
###
###elif playerVal < 21:
###     print("You Lose!")
###
###elif playerVal > Dealer_Value:
###     print("You Win!")
###
###elif playerVal < Dealer_Value:   
###     print("You lose!")

#performs program based on player's input/move

##gameMain()