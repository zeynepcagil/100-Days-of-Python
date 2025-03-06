
bidders=False

def max_bid(bidding_dict):
    winner=""
    highest_bid=0

    for bidder in bidding_dict:
        bid_amount=bidding_dict[bidder]
        if bid_amount>highest_bid:
            highest_bid=bid_amount
            winner=bidder

    print(f"The winner is {winner} with a bid of {highest_bid}")


bids = {}
while bidders==False:
    name=input("What is your name?")
    price=int(input("What is your bid? :"))
    otherBidders=input("Are there any other bidders? Type 'yes or 'no'.")
    bids[name] = price
    if otherBidders=="no":

        bidders=True
        max_bid(bids)
    elif otherBidders=="yes":
        print("\n" *20)



