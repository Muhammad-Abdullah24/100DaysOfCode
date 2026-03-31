from art import logo

print(logo)
print()
print("Welcome to the secret digital Blind Auction!!!")
not_done = True
auction = {}

while not_done:
    # TODO-1: Ask the user for input

    name = input("Please enter your name: ")
    bid = int(input("Please enter your bid: "))


    # TODO-2: Save data into dictionary {name: price}

    auction[name] = bid

    # TODO-3: Whether if new bids need to be added

    choice = input("Are there any more bidders('yes' or 'no'): ")
    if choice.lower() == "no":
        not_done = False
    else:
        print("\n" * 100)

# TODO-4: Compare bids in dictionary

highest_bid = 0
for key in auction:
    if auction[key] > highest_bid:
        highest_bid = auction[key]
        highest_bidder = key

print(highest_bidder + " is the winner with a bid of " + str(highest_bid))
