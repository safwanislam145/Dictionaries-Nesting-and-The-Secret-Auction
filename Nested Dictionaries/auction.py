
import os

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)

bids = {}
bidding = True

while bidding:
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))
    bids[name] = bid
    more_bids = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if more_bids == "no":
        bidding = False
    elif more_bids == "yes":
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        print("Invalid input. Please try again.")

highest_bid = 0
highest_bidder = ""

for bidder in bids:
    if bids[bidder] > highest_bid:
        highest_bid = bids[bidder]
        highest_bidder = bidder 

print(f"The winner is {highest_bidder} with a bid of ${highest_bid}.")