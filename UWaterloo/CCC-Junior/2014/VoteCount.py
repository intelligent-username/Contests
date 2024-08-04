# Vote Count: COMPLETE
# https://cemc.uwaterloo.ca/contests/computing/past_ccc_contests/2014/stage%201/juniorEn.pdf #2

V = int(input()) # Total number of votes
votes = input()

A = 0
B = 0

for x in votes:
    if x == "A":
        A += 1
    else:
        B += 1

if A > B:
    print('A')
elif B > A:
    print('B')
else:
    print('Tie')
