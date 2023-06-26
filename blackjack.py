from random import choice
from art import logo
from clear_screen import clear_screen

def get_cards():
    cards = [2,3,4,5,6,7,8,9,10,10,10,10,11]
    return choice(cards)

def get_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def get_result(player_score,dealer_score):
    global total_money,bid_amount
    if player_score == dealer_score:
        return f"Draw 🙃, you still have ${total_money} in you stock 😌"
    elif dealer_score == 0:
        total_money -= bid_amount
        return f"Lose, opponent has Blackjack 😱, your available balance of ${total_money} 😭"
    elif player_score == 0:
        total_money += bid_amount  
        return f"Win with a Blackjack 😎, now you have ${total_money} in your stock 😍"
    elif player_score > 21:
        total_money -= bid_amount
        return F"You went over. You lose 😭, your available balance of ${total_money} 😥"
    elif dealer_score > 21:
        total_money += bid_amount
        return f"Opponent went over. You win 😁, now you have ${total_money} in your stock 🥰"
    elif player_score > dealer_score:
        total_money += bid_amount
        return f"You win 😃, you stock become ${total_money} with win 😊"
    else:
        total_money -= bid_amount
        return f"You lose 😤, you have only ${total_money} in your stock 😞"
        

def play_game():
    print(logo)
    player_cards = []
    dealer_cards = []
    play_more = True

    for _ in range(2):
        player_cards.append(get_cards())
        dealer_cards.append(get_cards())

    while play_more:
        player_score = get_score(player_cards)
        dealer_score = get_score(dealer_cards)
        print(f"Your cards = {player_cards}, Your score = {player_score}")
        print(f"Dealer's first card = {dealer_cards[0]}")

        if player_score == 0 or dealer_score == 0 or player_score > 21:
            play_more = False
        else:
            if input("Type 'y' to get another card, type 'n' to pass: ").lower() == 'y':
                player_cards.append(get_cards())
            else:
                play_more = False
    
    while dealer_score != 0 and dealer_score < 17:
        dealer_cards.append(get_cards())
        dealer_score = get_score(dealer_cards)
    
    print(f"Your final hand: {player_cards}, final score: {player_score}")
    print(f"Dealer's final hand: {dealer_cards}, final score: {dealer_score}")
    print(get_result(player_score,dealer_score))


total_money = 1000
bid_amount = 0
while total_money > 0 and input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == 'y':
    bid_amount = abs(int(input(f"You have ${total_money} in your stock, enter the bid amount : $")))
    if bid_amount > total_money:
        print(f"You don't have ${bid_amount}, bid as per your stock 😕")
    else:
        clear_screen()
        play_game()