import random 

def random_card():
    return random.choice([
        2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11
    ])

def dealer_bust(card):
    hand = [card, random_card()]
    while sum(hand) < 17:
        hand.append(random_card())
    print(hand)
    return sum(hand) > 21

card = int(input("face up card: "))
        
print(f"bust: {dealer_bust(card)}")

#exceptions:
#   1. ace counts as 11 only