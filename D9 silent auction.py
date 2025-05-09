# This is an application that runs as a silent auction

print("Welcome to the silent auction")
print("We will now take the first bid")

auction_state = True
highest_bid = 0
highest_bid_name = ""

while auction_state:
    bidder_name = str(input("Bidder name: "))
    new_bid = int(input("Bid price: "))
    more_bidder = input("Are there more bidders ?(y/n)").lower()
    if new_bid > highest_bid:
        highest_bid = new_bid
        highest_bid_name = bidder_name
    if more_bidder == "n":
        auction_state = False
print(f"The highest bid was from {highest_bid_name} with a bid of${highest_bid}")
print("Congrats on your new item")
