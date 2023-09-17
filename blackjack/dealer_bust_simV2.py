import random

card_values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

def random_card():
    return random.choice(card_values)

def dealer_bust(card):
    hand = [card, random_card()]
    while sum(hand) < 17:
        hand.append(random_card())
    return sum(hand) > 21

def calc_probability(card, iterations):
    busts = 0
    for _ in range(iterations):
        if dealer_bust(card):
            busts += 1
    bust_probability = (busts/iterations)*100
    return busts, bust_probability

try:
    card = int(input("enter face up card (2-11): "))
    if card <2 or card > 11:
        raise ValueError("face up card must be between 2 and 11")
    iterations = int(input("enter number of iterations: "))
    
    busts, bust_probability = calc_probability(card, iterations)
    
    print(f"busts: {busts}")
    print(f"bust probability: {bust_probability:.2f}%")

except ValueError as e:
    print(f"error as {e}")