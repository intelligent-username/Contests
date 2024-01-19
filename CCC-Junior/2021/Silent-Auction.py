# Silent Auction: COMPLETE
# https://www.cemc.uwaterloo.ca/contests/computing/past_ccc_contests/2021/ccc/juniorEF.pdf #2

N = int(input("Number of people: "))
bids = {}
highest = 0

for i in range(N):
  name = input("Name: ")
  bid = int(input("Bid: "))
  bids[name] = bid
  if bid > highest:
    highest = bid

name = ""

for i in bids:
  print(i)
  if bids[f"{i}"] == highest:
    name = i
    break

print(f"The winner is {name} with a bid of {highest}")
