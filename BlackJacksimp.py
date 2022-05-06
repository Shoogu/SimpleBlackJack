'''COMPLETED VERSION'''
import random

print(".------.            _     _            _    _            _\n"
      "|A_  _ |.          | |   | |          | |  (_)          | |  \n"
      "|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __\n"
      "| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /\n"
      "|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   <\n"
      "`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_|\n"
      "      |  \/ K|                            _/ |                \n "
      "      `------'                          |__/           \n"
      "               WELCOME TO THE BLACK JACK CASINO               \n")

card_faces = ['A', '2', '3', '4', '5',
              '6', '7', '8', '9', '10', 'J', 'Q', 'K']
'''list storing all the possible Card Faces/Values'''

def deal_card():
    card_chosen = random.choice(card_faces)
    return card_chosen


def scoreboard():
    global player_3_or_more_hand, dealer_3_or_more_hand, player_total, dealer_total
    player_3_or_more_hand = ", ".join(players_hand)
    dealer_3_or_more_hand = ", ".join(dealers_hand)
    player_total = card_total(players_hand)
    dealer_total = card_total(dealers_hand)
    print(f"Player's Hand: {player_3_or_more_hand} || "
          f"Dealer's Hand: {dealer_3_or_more_hand}")
    print(f"☾{player_total}☽\t\t\t\t\t☾{dealer_total}☽")


game_over = False
bank = 900

while not game_over:
    if bank <= 0:
        game_over = True
        print("You're out of money, Game Over bud.")
        exit()

    bet_amount = input(f"Your current balance is ${bank}, BETTING OPTIONS:\n"
                       f"1. Input desired bet amount OR\n"
                       f"2. Type 'A' for ALL-IN (Your entire balance)\n"
                       f"Bet: $")

    if bet_amount in ['a', 'A']:
        bet_amount = bank
        bank = 0
    else:
        bank -= int(bet_amount)

    dealers_hand = []
    players_hand = []

    for _ in range(2):
        new_card1 = deal_card()
        dealers_hand.append(new_card1)
        new_card2 = deal_card()
        players_hand.append(new_card2)

    print(f"Player's Hand: {players_hand[0]}, {players_hand[1]} || "
          f"Dealer's Hand: {dealers_hand[0]}, ⬜")
    '''Opponents hand is hidden, thus the gambling begins!'''

    # for card score total
    def card_total(hand):
        total = 0
        aces = 0
        for card in range(0, len(hand)):
            if hand[card] in ['J', 'Q', 'K']:
                hand[card] = '10'
            elif hand[card] in ['A']:
                aces += 1
                continue
            total += int(hand[card])
        while True:
            if aces > 0:
                if (21 - total) >= (aces * 11):
                    total += 11
                else:
                    total += 1
                aces -= 1
            else:
                break
        return total
    '''The card distribution takes account whether the value of Aces should be ones
    or 11's, it must change depending on the current hand'''

    player_total = card_total(players_hand)
    dealer_total = card_total(dealers_hand)
    print(f"☾{player_total}☽\t\t\t\t\t☾{dealers_hand[0]}☽")

    # Decision Tree for Betting and Card Values
    if player_total == 21:
        if player_total == dealer_total:
            print("DRAW\n")
        else:
            print("PLAYER WINS\n")
            bank += (2 * int(bet_amount))
    elif player_total > 21:
        print("HOUSE WINS!\n")
    else:
        hit_or_stand = input("Would you like to 'Hit+' or 'Stand🧍'?: ").lower()
        while hit_or_stand.startswith('h'):
            players_hand.append(deal_card())
            player_3_or_more_hand = ", ".join(players_hand)
            dealer_3_or_more_hand = ", ".join(dealers_hand)
            player_total = card_total(players_hand)
            dealer_total = card_total(dealers_hand)
            if player_total == 21:
                if player_total == dealer_total:
                    scoreboard()
                    print("DRAW!\n")
                    bank += int(bet_amount)
                    break
                else:
                    scoreboard()
                    print("PLAYER WINS!\n")
                    bank += (2 * int(bet_amount))
                    break
            elif player_total > 21:
                scoreboard()
                print("HOUSE WINS!\n")
                break
            else:
                print(f"Player's Hand: {player_3_or_more_hand} || "
                      f"Dealer's Hand: {dealers_hand[0]}, ⬜")
                print(f"☾{player_total}☽\t\t\t\t\t☾{dealers_hand[0]}☽")
                hit_or_stand = input("Would you like to 'Hit+' or 'Stand🧍'?: ").lower()
                '''hit or stand function determines the user's following move, also adds to
                the opposing computer's hand'''

        if hit_or_stand.startswith('s'):
            scoreboard()
            if dealer_total == 21:
                dealer_3_or_more_hand = ", ".join(dealers_hand)
                player_3_or_more_hand = ", ".join(players_hand)
                dealer_total = card_total(dealers_hand)
                player_total = card_total(players_hand)
                scoreboard()
                if dealer_total == player_total:
                    print("DRAW!\n")
                    bank += int(bet_amount)
                    continue
                else:
                    print("HOUSE WINS!\n")
                    continue
            elif player_total < dealer_total <= 21:
                print("HOUSE WINS!\n")
                continue
            elif dealer_total < 17:
                while dealer_total < 17:
                    dealers_hand.append(deal_card())
                    dealer_3_or_more_hand = ", ".join(dealers_hand)
                    player_3_or_more_hand = ", ".join(players_hand)
                    dealer_total = card_total(dealers_hand)
                    player_total = card_total(players_hand)
                    scoreboard()
                    if player_total == 21:
                        if player_total == dealer_total:
                            scoreboard()
                            print("DRAW!\n")
                            bank += int(bet_amount)
                            break
                        else:
                            print("PLAYER WINS!\n")
                            bank += (2 * int(bet_amount))
                            break
                    elif dealer_total > 21:
                        print("PLAYER WINS!\n")
                        bank += (2 * int(bet_amount))
                        break
                    elif player_total > dealer_total:
                        print("PLAYER WINS!\n")
                        bank += (2 * int(bet_amount))
                        break
                    elif player_total < dealer_total <= 21:
                        print("HOUSE WINS!\n")
                        break
                    else:
                        print("PLAYER WINS!\n")
                        bank += (2 * int(bet_amount))
                        break
