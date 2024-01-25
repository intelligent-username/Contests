# Lunch Concert: INCOMPLETE
# https://cemc.uwaterloo.ca/contests/computing/past_ccc_contests/2021/ccc/seniorEF.pdf #3

N = int(input())
inputs = []

# Let i be friend number
for i in range(N):
    list = list(map(int, input.split()))
    # The input will contain P, W, and D. Each is in reference to friend 'i'
    # P: Position (metres away)
    # W: Walking speed, one metre per W seconds.
    # D: Can hear music D metres away from P 
    inputs.append(list)

# NEED TO FIND c, which is the point along the number line at which all friends can hear. 
# Goal: minimize the sum total of how long all of the friends have to walk
# IDEK where to start