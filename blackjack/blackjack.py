import random

# Define card values and suits
SUITS = ["♥", "♦", "♣", "♠"]
VALUES = [2, 3, 4, 5, 6, 7, 8, 9, 10, "King", "Queen", "Jack", "Ace"]

# Function to create a standard deck
def create_deck():
    return [(value, suit) for suit in SUITS for value in VALUES]

# Function to shuffle the deck
def shuffle_deck(deck):
    random.shuffle(deck)

#Function to display the player's and dealer's hands    
def display_hands(player_hand, dealer_hand):
    print(f"\nYour hand: {', '.join(map(str, player_hand))}")
    print(f"Dealer's hand: {', '.join(map(str, dealer_hand))}")

# Function to initialize the player's hand
def init_player(deck):
    return [deck.pop(), deck.pop()]

# Function to initialize the dealer's hand
def init_dealer(deck):
    return [deck.pop(), deck.pop()]

# Function to manage player's balance (stub)
def manage_player_balance(player_balance, player_bet, winner, player_blackjack):
    if winner == "Player":
        player_balance += player_bet*2
    elif player_blackjack == True:
        player_balance += player_bet*1.5
    elif winner == "Tie":
        return player_balance
    else:
        player_balance -= player_bet
    return player_balance

# Function to get the player's bet
def get_player_bet():
    return float(input("Enter the amount you want to bet: "))

# Function to perform a hit
def hit(deck, hand):
    hand.append(deck.pop())

# Function for the dealer's turn
def dealer_turn(deck, dealer_hand):
    while calc_hand(dealer_hand) < 17:
        hit(deck, dealer_hand)
    return bust(calc_hand(dealer_hand))


# Function to calculate the hand total
def calc_hand(hand):
    total = 0
    aces = 0

    for card in hand:
        value = card[0]
        if value in ["King", "Queen", "Jack"]:
            total += 10
        elif value == "Ace":
            total += 11
            aces += 1
        else:
            total += int(value)

    # Adjust for aces if total is greater than 21
    while total > 21 and aces > 0:
        total -= 10
        aces -= 1

    return total

# Function to check for a blackjack
def blackjack(hand, total):
    return len(hand) == 2 and total == 21

# Function to check for a bust
def bust(total):
    return total > 21

#Function to check for a winner    
def determine_winner(player_total, dealer_total):
    if player_total > dealer_total:
        return "Player"
    elif dealer_total > player_total:
        return "Dealer"
    else:
        return "Tie"

# Function to play blackjack
def play_blackjack():
    deck = create_deck()
    shuffle_deck(deck)
    
    player_balance = float(input("Enter your starting balance: "))
    
    while player_balance > 0:
        print(f"Your balance: {player_balance}")
        player_bet = get_player_bet()
    
        player_hand = init_player(deck)
        dealer_hand = init_dealer(deck)
        print(f"\nYour hand: {player_hand[0]}, {player_hand[1]}")
        print(f"Dealer's hand: {dealer_hand[0]}\n")
        
        while True:
            total = calc_hand(player_hand)
            print(f"Your total: {total}")
        
            player_blackjack = blackjack(player_hand, total)
        
            choice = str(input("Do you want to hit(h) or stand(s)? -> "))
        
            if choice == "h" or choice == "hit":
                hit(deck, player_hand)
                total = calc_hand(player_hand)
                print(f"\nYour hand: {', '.join(map(str, player_hand))}")
                print(f"Dealer's hand: {dealer_hand[0]}")
                print(f"Your total: {total}")
                if bust(total):
                    player_balance = manage_player_balance(player_balance, player_bet, "Dealer", player_blackjack)
                    print("You busted!")
                    break
            elif choice == "s" or choice == "stand":
                dealer_turn(deck, dealer_hand)
                display_hands(player_hand, dealer_hand)
                
                player_total = calc_hand(player_hand)
                dealer_total = calc_hand(dealer_hand)
                winner = determine_winner(player_total, dealer_total)
                
                if player_blackjack:
                    print("Blackjack woohooooo!")
                    player_balance = manage_player_balance(player_balance, player_bet, winner, player_blackjack)
                elif winner == "Tie":
                    print("It's a tie!")
                    player_balance = manage_player_balance(player_balance, player_bet, winner, player_blackjack)
                elif dealer_turn(deck, dealer_hand):
                    print("The Dealer busted!")
                    player_balance = manage_player_balance(player_balance, player_bet, "Player", player_blackjack)
                else:
                    print(f"{winner} wins!")
                    player_balance = manage_player_balance(player_balance, player_bet, winner, player_blackjack)
                    
                if player_balance == 0:
                    return False
                break
            
            elif choice == "quit":
                print("Bye.")
                return False
          
if __name__ == "__main__":
    play_blackjack()
