import random
import json

# list of cards
with open("card.json", encoding="UTF-8") as f:
    Cards = json.load(f)
# User input to start the game
# start_game = input("Start game?[Y/N] -> ")

# creating empty list so it can be accessed anywhere in the code

shuffle_set = []
player_cards = []
dealer_cards = []
dealer_cards1 = []
Aces = ["A♠", "A♥", "A♣", "A♦"]
# Initializing each value
playerVal = 0
dealerValue = 0
dealerValue1 = 0

move = "hit"

#function for player move
def playerMove():
    global move
    global index
    global playerVal
    global dealerValue
    global dealerValue1

    while move == "hit":
        move = input("What's the move?(Hit/Stand) --> ").lower()

        if move == "hit":
            player_card_value = player_cards[len(player_cards) - 1][0]
            player_cards.append(random.choice(Cards))
            shuffle(player_cards)
            if (
                player_card_value == "1"
                or player_card_value == "J"
                or player_card_value == "Q"
                or player_card_value == "K"
            ):
                playerVal += 10
                print(player_cards[len(player_cards) - 1], "\n")
                print(f"your hand: {' '.join(player_cards)} ({playerVal}) \n")

            elif (
                player_card_value != "1"
                and player_card_value != "J"
                and player_card_value != "Q"
                and player_card_value != "K"
                and player_card_value != "A"
            ):
                player_card_value = int(player_card_value)
                playerVal += player_card_value
                print(player_cards[len(player_cards) - 1], "\n")
                print(f"your hand: {' '.join(player_cards)} ({playerVal}) \n")

            elif player_card_value == "A":
                playerVal += 11
                print(player_cards[len(player_cards) - 1], "\n")
                print(f"your hand: {' '.join(player_cards)} ({playerVal}) \n")
        
        elif any(Card in player_cards for Card in Aces) and playerVal < 21:
            playerVal -= 11
            playerVal += 1

        elif playerVal >= 21:
            break

        else:
            print("Please enter valid keyphrase: hit or stand \n")

    return player_cards, playerVal

#deal cards until 17 or higher for dealer
def dealerMove():
    global Dealer_Val

    while Dealer_Val < 17:
        dealer_card1_value = dealer_cards1[len(dealer_cards1) - 1][0]
        dealer_cards1.append(random.choice(Cards))
        shuffle(dealer_cards1)
        if (
            dealer_card1_value == "1"
            or dealer_card1_value == "J"
            or dealer_card1_value == "Q"
            or dealer_card1_value == "K"
        ):
            Dealer_Val += 10

        elif (
            dealer_card1_value != "1"
            and dealer_card1_value != "J"
            and dealer_card1_value != "Q"
            and dealer_card1_value != "K"
            and dealer_card1_value != "A"
        ):
            dealer_card1_value = int(dealer_card1_value)
            Dealer_Val += dealer_card1_value

        elif dealer_card1_value == "A":
            Dealer_Val += 11
        
        elif any(Card in Aces for Card in dealer_cards1) and DealerVal > 21:
            DealerVal -= 11
            DealerVal += 1

    return Dealer_Val

#picking random cards from the deck  
#and removing them to avoid repetition
def shuffle(set):
    for i in range(len(set)):
        if set[i] in Cards:
            index = Cards.index(set[i])
            Cards.remove(Cards[index])
    return Cards

# game flow
##def gameMain():
##    global playerVal
##    global dealerValue
##    global dealerValue1
##    while start_game == "Y":

# Shuffle and dealing of cards
shuffle_set.extend(random.sample(Cards, 4))
player_cards.extend(random.sample(shuffle_set, 2))
dealer_cards.append(random.choice(shuffle_set))
dealer_cards1.append(random.choice(shuffle_set))
shuffle(shuffle_set)


# Calculating the value of player's hand

for Card in player_cards:
    player_card_value = Card[0]
    if (
        player_card_value == "1"
        or player_card_value == "J"
        or player_card_value == "Q"
        or player_card_value == "K"
    ):
        playerVal += 10
    elif (
        player_card_value != "1"
        and player_card_value != "J"
        and player_card_value != "Q"
        and player_card_value != "K"
        and player_card_value != "A"
    ):
        player_card_value = int(player_card_value)
        playerVal += player_card_value
    elif player_card_value == "A":
        playerVal += 11

dealer_card_value = dealer_cards[0][0]
if (
    dealer_card_value == "1"
    or dealer_card_value == "J"
    or dealer_card_value == "Q"
    or dealer_card_value == "K"
):
    dealerValue += 10
elif (
    dealer_card_value != "1"
    and dealer_card_value != "J"
    and dealer_card_value != "Q"
    and dealer_card_value != "K"
    and dealer_card_value != "A"
):
    dealer_card_value = int(dealer_card_value)
    dealerValue += dealer_card_value
elif dealer_card_value == "A":
    dealerValue += 11

dealer_card1_value = dealer_cards1[0][0]
if (
    dealer_card1_value == "1"
    or dealer_card1_value == "J"
    or dealer_card1_value == "Q"
    or dealer_card1_value == "K"
):
    dealerValue1 += 10
elif (
    dealer_card1_value != "1"
    and dealer_card1_value != "J"
    and dealer_card1_value != "Q"
    and dealer_card1_value != "K"
    and dealer_card1_value != "A"
):
    dealer_card1_value = int(dealer_card1_value)
    dealerValue1 += dealer_card1_value
elif dealer_card1_value == "A":
    dealerValue1 += 11

Dealer_Val = dealerValue + dealerValue1

# Output each hand and it's value
print(f"dealer's hand: {''.join(dealer_cards)} x ({dealerValue})")
print(f"your hand: {' '.join(player_cards)} ({playerVal})")

playerMove()

dealerMove()

#win conditions
if playerVal == 21:
    print(
        f"Dealer: {' '.join(dealer_cards)} {' '.join(dealer_cards1)}, ({Dealer_Val}) \n"
    )
    print("Blackjack! You win!")

elif playerVal > 21:
    print(
        f"Dealer: {' '.join(dealer_cards)} {' '.join(dealer_cards1)}, ({Dealer_Val}) \n"
    )
    print("Bust! You lose!")

elif playerVal > Dealer_Val and playerVal < 21:
    print(
        f"Dealer: {' '.join(dealer_cards)} {' '.join(dealer_cards1)}, ({Dealer_Val}) \n"
    )
    print("You Win!")

elif playerVal < Dealer_Val: 
    print(
        f"Dealer: {' '.join(dealer_cards)} {' '.join(dealer_cards1)}, ({Dealer_Val}) \n"
    )
    print("You lose!")

