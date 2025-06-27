print("Welcome to the auction program!")
name = input("What is your name? ")
bid = float(input("What is your bid? $"))
 
auction = {
  name : bid
}

yes_no = input("Are there any other bidders? Type 'yes' or 'no': ")
while yes_no != "no":    
    name = input("What is your name? ")
    bid = float(input("What is your bid? $"))
    auction[name] = bid
    yes_no = input("Are there any other bidders? Type 'yes' or 'no': ")

print("The auction has ended. Here are the bids:")
for key in auction:
    print(f"{key}: ${auction[key]}")
#generate max value of the bids
winner, max_bid = max(auction.items(), key=lambda item: item[1])

print(f"The winner is {winner} with bid of: ${max_bid:.2f}")
