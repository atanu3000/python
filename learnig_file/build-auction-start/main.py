import art
print(art.logo)

new_bidders = {}

choice = ""
bidding_finished = False
while not bidding_finished:
    name = input("Enter your name: ")
    bid = int(input("Enter your bid amount: $"))
    new_bidders[name] = bid
    choice = input("Are there any other bidders? type 'yes' or 'no'.\n").lower()
    if choice == "no":
        bidding_finished = True
    
max = 0
name = ""
for bidder in new_bidders:
    if max < new_bidders[bidder]:
        max = new_bidders[bidder]
        name = bidder
print(f"The winner is {name} with a bid of {max}")
