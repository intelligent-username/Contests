# Winning Score; COMPLETE
# https://www.cemc.uwaterloo.ca/contests/computing/past_ccc_contests/2019/stage%201/juniorEF.pdf #1

# For each team, 
# The first line contains the number of successful 3-point shots
# The second line contains the number of successful 2-point field goals 
# The third line contains the number of successful 1-point free throws.

A = int(input()) * 3 + int(input()) * 2 + int(input())
B = int(input()) * 3 + int(input()) * 2 + int(input())

if A > B:
    print("A")
elif B > A:
    print("B")
else:
    print("T")
