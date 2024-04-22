import random
import time

def create_deck():
    #Creates a deck of 52 Cards
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
    deck = [{'suit': suit, 'rank': rank} for suit in suits for rank in ranks]
    #Uses random.shuffle to mix up the deck
    random.shuffle(deck)
    return deck

def card_value(card):
    #Reports a cards value
    rank_values = {
        'Ace': 11,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5,
        'Six': 6,
        'Seven': 7,
        'Eight': 8,
        'Nine': 9,
        'Ten': 10,
        'Jack': 10,
        'Queen': 10,
        'King': 10
        }
    return rank_values[card['rank']]

def hand_value(hand):
    #Reports a current hands value
    value = sum(card_value(card) for card in hand)
    num_aces = sum(1 for card in hand if card['rank'] == 'Ace')
    while value > 21 and num_aces:
        #if a hands value is over 21 an aces value turns into 1
        value -= 10
        num_aces -= 1
    return value

def play_blackjack():


    print("Welcome to Blackjack")
    time.sleep(2)
    print("")
    bank = float(input("How much is in your bank account?: "))
    time.sleep(2)
    print("")
    balance = float(input("How much are your bringing to the casino?: "))
    time.sleep(2)
    print("")
    while True:
        deck = create_deck()
        # Step 4: Check if the player has enough balance to continue
        if balance <= 0:
            if bank > 4:
                choice = input("You're out of money!. Are you going to the ATM?")
                if choice.lower() == "yes":
                    done = 0
                    print("")
                    print("There is a 4$ fee")
                    print("")

                    while done == 0:
                        print(f"Your balance is {bank}$")
                        withdraw = float(input("How much are withdrawing:"))
                        if withdraw == 0:
                            break
                        if (withdraw + 4) > bank:
                            print("Insufficient funds")
                        else:
                            done = 1
                            balance += withdraw
                            bank -= withdraw + 4

                else:
                    print("Game over")
                    break
            else:
                print("You have lost all your money, its over.")
                break


        # Step 2: Ask for the player's bet amount
        bet = float(input("Enter your bet for this hand: "))
        if bet > balance:
            print("You cannot bet more than your current balance. Please try again.")
            continue
        balance -= bet
        print("Bets are closed, now drawing cards...")
        print("")
        # .pop() method is used to "draw" a card from the deck by removing a card from the deck and adding it to a players hand
        player_hand = [deck.pop(), deck.pop()]
        dealer_hand = [deck.pop(), deck.pop()]
        time.sleep(2)
        # Displaying the initial hands
        print(f"Dealer shows a {dealer_hand[0]['rank']} of {dealer_hand[0]['suit']}")
        print("")
        time.sleep(2)
        print(f"Your first card is {player_hand[0]['rank']} of {player_hand[0]['suit']}")
        print("")
        time.sleep(2)
        print(f"Your second card is {player_hand[1]['rank']} of {player_hand[1]['suit']}")
        print("")
        time.sleep(2)
        player_hand_description = " and ".join(f"{card['rank']} of {card['suit']}" for card in player_hand)
        print(f"Dealer is showing a {dealer_hand[0]['rank']} of {dealer_hand[0]['suit']}")
        print(f"Your hand: {player_hand_description} (Hand Value: {hand_value(player_hand)})")
        print("")
        dealer_hand_description = " and ".join(f"{card['rank']} of {card['suit']}" for card in dealer_hand)
        # Player's turn
        while hand_value(player_hand) < 21:
            action = input("Do you want to hit or stand? ")
            if action.lower() == 'hit':
                print("Drawing...")
                time.sleep(2)
                new_card = deck.pop()
                new_card_description = f"{new_card['rank']} of {new_card['suit']}"
                print(f"You drew a {new_card_description}")
                player_hand.append(new_card)
                player_hand_description = " and ".join(f"{card['rank']} of {card['suit']}" for card in player_hand)
                time.sleep(1)
                print(f"Your hand: {player_hand_description} (Hand Value: {hand_value(player_hand)})")
                print("")
            elif action.lower() == 'stand':
                print("")
                break

        # Dealer's turn (revealed after player's turn if player hasn't busted)

        if hand_value(player_hand) <= 21:
            dealer_hand_description = " and ".join(f"{card['rank']} of {card['suit']}" for card in dealer_hand)
            print("Dealer is flipping...")
            time.sleep(2)
            print(f"Dealer draws a {dealer_hand[1]['rank']} of {dealer_hand[1]['suit']}")
            time.sleep(1)
            print(f"Dealer's hand: {dealer_hand_description} (Hand Value: {hand_value(dealer_hand)})")
            print("")
            i = 2
            while hand_value(dealer_hand) < 17:
                dealer_hand.append(deck.pop())
                dealer_hand_description = " and ".join(f"{card['rank']} of {card['suit']}" for card in dealer_hand)
                print("Dealer is hitting...")
                print("")
                time.sleep(3)
                print(f"Dealer draws a {dealer_hand[i]['rank']} of {dealer_hand[i]['suit']}")
                time.sleep(2)
                print(f"Dealers hand: {dealer_hand_description} (Hand Value: {hand_value(dealer_hand)})")
                i += 1
                time.sleep(3)
                print("")

        # Determine the winner

        player_value = hand_value(player_hand)
        dealer_value = hand_value(dealer_hand)
        time.sleep(1)
        print("")
        print("Final hands:")
        time.sleep(1)
        print(f"Your hand: {player_hand_description} (Hand Value: {player_value})")
        print(f"Dealer's hand: {dealer_hand_description} (Hand Value: {dealer_value})")
        time.sleep(1)
        print("")
        if player_value > 21:
            print("You bust! Dealer wins.")
        elif dealer_value > 21 or player_value > dealer_value:
            print("You win!")
            balance += bet * 2
        elif player_value < dealer_value:
            print("Dealer wins.")
        else:
            print("It's a push.")
            balance += bet
        print("")
        time.sleep(2)
        print(f"Your current balance is {balance}")

if __name__ == "__main__":
    play_blackjack()
