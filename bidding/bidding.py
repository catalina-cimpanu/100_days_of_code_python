import os
clear = lambda: os.system('cls')
participants = []

another_bidder = True
while another_bidder == True:
    name = input("What is your name?\n")
    bid = input("How much do you want to bid?\n")
    bidder = {
        "name": name,
        "bid": bid
        }
    participants.append(bidder)
    clear()
    x = input("Does anyone else want to bid? Type 'yes' or 'no'\n").lower()
    if x == "no":
        another_bidder = False
    elif x == "yes":
        another_bidder = True
    else:
        x = input("Please gie a valid answer Type 'yes' or 'no'\n").lower()

print(participants)

max_bid = 0
winner = ""
for participant in participants:
    bid = int(participant["bid"])
    if bid > max_bid:
        max_bid = bid
        winner = participant["name"]

print(f"The winner is {winner}!")
