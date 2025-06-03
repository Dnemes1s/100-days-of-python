import random

def win_lose(player, comp):

    if player > 21:
        print("You bust. House wins\n")
        return False

    elif comp > 21:
        print("You win. House bust\n")
        return False

    elif player and comp >= 21:
        print("No one wins\n")
        return False

    elif player == 21:
        print("You hit black jack !!!\n")
        return False

    elif comp == 21:
        print("House hit black jack. You lose\n")
        return False
    
    return True

print("Welcome to blackjack")
print("Im sure you know the rules alredy, so lets get started")

play = True
round = 0
player_hand = [random.randint(1,11),random.randint(1,11)]
computer_hand = [random.randint(1,11),random.randint(1,11)]

ph_sum = int(player_hand[0] + player_hand[1])
ch_sum = int(computer_hand[1])
ch_sum_check = (computer_hand[0] + computer_hand[1])

while play:
    print("Current  cards")
    print("")
    print(f"your hand is: {player_hand} total = {ph_sum}")
    print(f"Computers hand is: [* {computer_hand[1:]}] total = {ch_sum}")
    print(f"{computer_hand} {ch_sum_check}")


    
    hit_or_stand = input("What would you like to do ? (Hit or stand)\n").lower()
    if hit_or_stand == 'hit':


        card_player = random.randint(1,11)
        card_comp = random.randint(1,11)
        print(f"Heres your extra card {card_player}")

        player_hand.append(card_player)
        computer_hand.append(card_comp)

        ph_sum = sum(player_hand)
        ch_sum = sum(computer_hand)

        play = win_lose(ph_sum, ch_sum)
    
    else:
        card_comp = random.randint(1,11)
        computer_hand.append(card_comp)

        ph_sum = sum(player_hand)
        ch_sum = sum(computer_hand)

        play = win_lose(ph_sum, ch_sum)

print(f"Your final cards: {player_hand} {ph_sum}")
print(f"Computer final cards: {computer_hand} {ch_sum}")






