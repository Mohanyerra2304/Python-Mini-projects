import os
from art import logo
print(logo)

bids = {}
bidding_finished = False

def highest_bidder(bidding_record):
  highest_bid = 0
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")    
while not bidding_finished:
  name = input("what's your name? : ")
  price = int(input("what is your bid? :$"))
  bids[name]=price
  should_continue = input("Are there any other bidder? Type 'yes' or 'no' : ").lower()
  print()
  if should_continue == "no" :
    bidding_finished = True
  elif should_continue == "yes":
    os.system('clear')
    
highest_bidder(bids)
  