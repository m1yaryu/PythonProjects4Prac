import random

#list of cards
Cards = {"A♠, 2♠, 3♠, 4♠, 5♠, 6♠, 7♠, 8♠, 9♠, 10♠, J♠, Q♠, K♠, A♥, 2♥, 3♥, 4♥, 5♥, 6♥, 7♥, 8♥, 9♥, 10♥, J♥, Q♥, K♥, A♣, 2♣, 3♣, 4♣, 5♣, 6♣, 7♣, 8♣, 9♣, 10♣, J♣, Q♣, K♣, A♦, 2♦, 3♦, 4♦, 5♦, 6♦, 7♦, 8♦, 9♦, 10♦, J♦, Q♦, K♦"}

dealer_cards = ""
player_cards = ""

for i in range(2):
    dealer_cards += random.choices(Cards)
    player_cards += random.choices(Cards)

print(dealer_cards)
print(player_cards)
#code for the actual game
#def game_main():
#    while True:
#        print("Dealer: ")
#        print("You: ")
#

#starting code
#def game_start():
#    gameStart = input("Start?")
#    if gameStart == True:
#        return gameStart
#    else:
 #       return 0

#game_start()
#if gameStart == True:
#    game_main()