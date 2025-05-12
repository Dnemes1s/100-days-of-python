bidders = {

}

def highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    
    print(f"The winner is {winner} with a bid amount of ${highest_bid}")


gavel = '''                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\
    
                       .-------------.
                      /_______________\
                    
'''

print(gavel)
print("Welcome to the silent auction\n" \
"Now accepting bids")

more_users = True

while more_users:
    name = input("Who is bidding ? ")
    bid = int(input("Bid amount: $"))
    bidders[name] = bid
    cont = input("Are there more bidders? (y/n)").lower()
    print("\n" *20)
    if cont == "n":
        more_users = False
        highest_bidder(bidders)



