# This is an application that runs as a silent auction

print("Welcome to the silent auction")
print("We will now take the first bid")

auction_state = True    # Sets while loop condition
highest_bid = 0     # keeps the highest bid
highest_bid_name = ""   # Keeps the name of the highest bidder

while auction_state:
    bidder_name = str(input("Bidder name: "))
    new_bid = int(input("Bid price: "))
    more_bidder = input("Are there more bidders ?(y/n)").lower()    # Checks if there are more bidders
    
    if new_bid > highest_bid:   # Checks if the latest bid is higher than the previous one 
        highest_bid = new_bid   # Updates the highest
        highest_bid_name = bidder_name  # changes the name to the highest bidder

    if more_bidder == "n":  # Checks if there are more bidders
        auction_state = False   # Sets the auction state to false to escape the while loop

print(f"The highest bid was from {highest_bid_name} with a bid of${highest_bid}")   # Displays the highest bidder and the bid price
print("Congrats on your new item")
