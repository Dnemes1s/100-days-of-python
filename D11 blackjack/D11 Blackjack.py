import random

def win_lose(player, comp):
    if player and comp > 21:
        print("No one wins\n")
        return False

    elif player > 21:
        print("You bust. House wins\n")
        return False

    elif comp > 21:
        print("You win. House bust\n")
        return False

    elif player == 21:
        print("You hit black jack !!!\n")
        return False

    elif comp == 21:
        print("House hit black jack. You lose\n")
        play = False
        return play

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
ph_sum = int()
ch_sum = int()

while play:
    print("Current  cards")
    print("")
    print(f"{player_hand} {ph_sum}")
    print(f"{computer_hand} {ch_sum}")


    
    hit_or_stand = input("What would you like to do ? (Hit or stand)").lower()
    if hit_or_stand == 'hit':


        card_player = random.randint(1,11)
        card_comp = random.randint(1,11)
        print(f"Heres your extra card {card_player}")

        player_hand.append(card_player)
        computer_hand.append(card_comp)

        ph_sum = sum(player_hand)
        ch_sum = sum(computer_hand)

        win_lose(ph_sum, ch_sum)

        play = win_lose
        






