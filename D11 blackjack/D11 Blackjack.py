import random

print("Welcome to blackjack")
print("Im sure you know the rules alredy, so lets get started")

play = True
round = 0
player_hand = []
computer_hand = []

card_player = random.randint(1,11)
card_comp = random.randint(1,11)

player_hand.append(card_player)
computer_hand.append(card_comp)

while play:

    print(player_hand)
    print(computer_hand)
    print("Current  cards")
    hit_or_stand = input("What would you like to do ? (Hit or stand)").lower()
    if hit_or_stand == 'hit':
        card_player = random.randint(1,11)
        card_comp = random.randint(1,11)
        print(f"Heres your extra card {card_player}")

        player_hand.append(card_player)
        computer_hand.append(card_comp)

        ph_sum = sum(player_hand)
        ch_sum = sum(computer_hand)

        print(f"Your total is {ph_sum}")
        print(f"Computer total is {ch_sum}")





