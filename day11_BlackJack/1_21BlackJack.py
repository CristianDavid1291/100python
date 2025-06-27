import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]  

def repartCards():
    hand = [random.choice(cards), random.choice(cards)]
    return hand

continue_playing = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
while continue_playing.lower() == 'y':
    player_cards = repartCards()
    dealer_cards = repartCards()
    player_score = sum(player_cards)
    dealer_score = sum(dealer_cards)
    print(f"Your cards: {player_cards}, current score: {sum(player_cards)}")
    print(f"Dealer's first card: {dealer_cards[0]}")
    
    while player_score < 21:
        should_continue = input("Type 'y' to get another card, type 'n' to pass: ")
        if should_continue.lower() == 'y':
            player_cards.append(random.choice(cards))
            player_score = sum(player_cards)
            print(f"Your cards: {player_cards}, current score: {player_score}")
        else:
            break
    if player_score > 21:
        print("You went over. You lose!")
    else:
        print(f"Your final hand: {player_cards}, final score: {player_score}")
        print(f"Dealer's cards: {dealer_cards}, final score: {dealer_score}")
        print(f"Winner is {'you' if player_score > dealer_score else 'dealer' if dealer_score > player_score else 'draw'}!")
    continue_playing = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    